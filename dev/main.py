from os import system
from dir_exist import dir_exist
from make_file import make_file
from config import (
    default_config_script,
    default_config_styles,
)
from settings import (
    default_app_favicon,
    list_directory_name,
    default_templete,
    default_styles,
    default_script,
)


if __name__ == "__main__":

    # Reading App name from user.
    user_input_app_name = input("\n:: Enter a App name:\n:: ")
    print()

    try:
        if " " not in user_input_app_name and "" != user_input_app_name:
            base_dir = user_input_app_name

            if base_dir not in dir_exist():
                # Creating default directorys.
                system(f"mkdir ./{base_dir}")
                for directory_name in list_directory_name:
                    system(f"mkdir ./{base_dir}/{directory_name}")

                # Creating default files.
                make_file(f"./{base_dir}/meta/config_styles.css", default_config_styles)
                make_file(f"./{base_dir}/meta/config_script.js", default_config_script)
                make_file(f"./{base_dir}/media/icons/favicon.svg", default_app_favicon)
                make_file(f"./{base_dir}/index.html", default_templete)
                make_file(f"./{base_dir}/styles/styles.css", default_styles)
                make_file(f"./{base_dir}/src/index.js", default_script)
                make_file(f"./{base_dir}/README.md", "## Write your app detailes.")

                # Success message.
                print(f"Your App has been created successfully and its name is `{base_dir}`.\n")

                # user input and checking for runn created App or not.
                is_run = input(":: Do you want to run it with live-server then press [y/n]:\n:: ")
                print()

                # Checking user input.
                if is_run.lower() == "y" or is_run.lower == "yes":
                    system(f"cd ./{base_dir} && live-server && cd ..")
                else:
                    print('Exit.\n')
            else:
                print(f"Oops! Your entered app name '{base_dir}' already exists. Please try another name.\n")
        else:
            print("Please! Enter a valid App name.\n")

    except Exception as err:
        print("Oops! Somthing is wrong: ", err)
        print()
