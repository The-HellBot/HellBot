import asyncio
import shlex
import sys


def read_requirements(file_path: str) -> list[str]:
    with open(file_path, "r") as file:
        return [line.strip() for line in file]


def compare_requirements(file1: str, file2: str) -> list[str]:
    requirements1 = set(read_requirements(file1))
    requirements2 = set(read_requirements(file2))

    return list(requirements1 ^ requirements2)


async def runcmd(cmd: str) -> tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )


async def update_requirements(deploy: str, plugins: str) -> None:
    modules = compare_requirements(deploy, plugins)
    try:
        for module in modules:
            await runcmd(f"pip install {module}")
            print(f">> Installed Requirement: {module}")
    except Exception as e:
        print(f"Error installing requirments: {str(e)}")


asyncio.run(update_requirements(sys.argv[1], sys.argv[2]))
