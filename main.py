from argparse import ArgumentParser
import asyncio
import logging
from pathlib import Path
import shutil


def parse_paths():
    parser = ArgumentParser(description="Sort files by extension asynchronously.")
    parser.add_argument("source_folder", type=str)
    parser.add_argument("output_folder", type=str)
    args = parser.parse_args()
    return Path(args.source_folder), Path(args.output_folder)


async def read_folder(folder: Path, dest_root: Path):
    for item in folder.iterdir():
        if item.is_dir():
            await read_folder(item, dest_root)
        elif item.is_file():
            await copy_file(item, dest_root)


async def copy_file(file: Path, dest_folder: Path):
    ext = file.suffix[1:] if file.suffix else "no_extension"
    dest_folder = dest_folder / ext
    dest_folder.mkdir(parents=True, exist_ok=True)
    dest_path = dest_folder / file.name

    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, shutil.copy2, file, dest_path)


async def main():
    source_path, output_path = parse_paths()

    if not source_path.exists():
        logging.error("Source folder does not exist.")
        return
    output_path.mkdir(parents=True, exist_ok=True)
    await read_folder(source_path, output_path)


if __name__ == "__main__":
    asyncio.run(main())
