try:
    #Writing to file (Creates new file automatically)
    with open("C:/Users/email/OneDrive/Desktop/Uma/work/DS2026/Week_03/report.txt","w") as f:
        f.write("TestCase1 - Passed\n")
        f.write("TestCase2 - Failed\n")
        f.write("TestCase3 - Passed\n")
    print("File write completed")

    #Appending content to the file
    with open("C:/Users/email/OneDrive/Desktop/Uma/work/DS2026/Week_03/report.txt","a") as f:
        f.write("TestCase4 - Passed\n")
        f.write("TestCase5 - Failed\n")
    print("File append completed")

    #Reading contents from file
    with open("C:/Users/email/OneDrive/Desktop/Uma/work/DS2026/Week_03/report.txt","r") as f:
        lines = f.readlines()
        for line in lines:
            print(line,end="")
        
        total_tests = len(lines)
        passed_count = 0
        failed_count = 0

        #Summary
        for line in lines:
            if "Passed" in line:
                passed_count = passed_count+1
            else:
                failed_count = failed_count+1
        print("\n\n--- Test Summary Report ---")
        print(f"Total Tests: {total_tests}")
        print(f"Passed: {passed_count}")
        print(f"Failed: {failed_count}")


except FileNotFoundError:
    print("File not found\n")
finally:
    print("isClosed : ",f.closed)