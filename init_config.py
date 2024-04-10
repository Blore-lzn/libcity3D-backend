import shutil


def init_config():
    # copy libcity task config
    shutil.copyfile(
        "./utils/Bigscity-LibCity/libcity/config/task_config.json",
        "./config/libcity.json",
    )


if __name__ == "__main__":
    print("init config")
    init_config()
