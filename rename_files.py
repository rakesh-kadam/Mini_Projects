import os
def rename_files():
    #(1) get the file name from a folder
    file_list = os.listdir("/home/rakesh/Desktop/Projects/Secret_message/prank/prank")
    #print(file_list)
    
    saved_path = os.getcwd()
    print("Current WorkingDirectory is "+ saved_path)
    os.chdir("/home/rakesh/Desktop/Projects/Secret_message/prank/prank")

    #(2)for each file,rename filename
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)

rename_files()