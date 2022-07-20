def update_from_repo(oldVer, newVer, git_url, installation_route, branch, reg = False):

    def folder_actions(fromPath, toPath, deleteFromPath=False, deleteVersionFile=False):
        from os.path import join
        from os import listdir, rmdir, remove
        from shutil import move

        for filename in listdir(fromPath):
            move(join(fromPath, filename), join(toPath, filename))

        if deleteFromPath: rmdir(fromPath)
        if deleteVersionFile:
            remove(f"{installation_route}\\version")
            remove(f"{installation_route}\\readme.md")

    from git_clone import git_clone
    git_clone(git_url, path=installation_route, branch_name=branch)
    
    folder_actions(installation_route + "\\pylox", installation_route, deleteFromPath=True, deleteVersionFile=True)
    if reg:
        print(f"Git files are now updated up to the version v{oldVer} --> v{newVer}")

