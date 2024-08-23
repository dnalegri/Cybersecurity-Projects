def main():
    try:
        with open("pythontest.txt", "w") as file:
            file.write("Using Python to output text file.")
    except IDError as e:
        print("Exception caught: Unable to write this file ", e)
    except Exception as e:
        print("Another error occurred ", e)
    else:
        print("File writen successfully")
if __name__ == "__main__":
    main()
