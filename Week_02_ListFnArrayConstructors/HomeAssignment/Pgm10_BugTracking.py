class BugTracker:
  #Create dictionary for bugs
    def __init__(self):
        self.bugs = {}
    
   #Add new bug 
    def add_bug(self,bug_id, description, severity):
        self.bugs [bug_id]= {
            "description" : description,
            "severity" : severity,
            "status" : "Open"
        }
        print("Added new bug :",bug_id)
    
    #Update bug status
    def update_status(self,bug_id,new_status):
        if bug_id in self.bugs:
            self.bugs[bug_id]["status"] = new_status
            print(f"Bug {bug_id} found and updated with new status : {new_status}")
        else:
            print(f"Bug id {bug_id} not found")
    
    #print all bugs
    def print_bugs(self):
        for keys,bug in self.bugs.items():
            print(f"{keys} | {bug} ")

if __name__ == "__main__":
    #Initializing class
    tracker = BugTracker()

    #Adding Bugs
    tracker.add_bug("BUG-001", "Service Unavailable", "High")
    tracker.add_bug("BUG-002", "Typo in footer", "Low")

    #Printing bugs
    print("\nCurrent Bugs:")
    tracker.print_bugs()

    #Updating Bug status
    tracker.update_status("BUG-002","In Progress")
    print("\nAfter Update:")
    tracker.print_bugs()