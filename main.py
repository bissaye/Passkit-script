import sys
import getopt
import Tools
import Services

if __name__ == '__main__':

    aide = False
    path = ""
    new_File = ""

    options, args = getopt.getopt(
        sys.argv[1:],
        "hp:n:",
        [
            "help",
            "path=",
            "name="
        ]
    )

    for option, arg in options:
        if option in ("-h", "--help"):
            aide = True
        elif option in ("-p", "--path"):
            path = arg
        elif option in ("-n", "--name"):
            new_File = arg


    if aide:
        Tools.help()
    else:
        if path == "":
            Services.Log.error(msg="file path is required")
        elif not Tools.Checking.check_if_path_exists(path=path) :
            Services.Log.error(msg="file path doesn't match any file")
        else:
            if new_File == "":
                new_File = "result.xlsx"
            Services.SendPasskit.send_passkit(path=path, new_File=new_File)
