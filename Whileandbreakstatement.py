while True:
    user_input = input("Enter yor name:")
    # terminate the loop when user enters end
    if user_input == "end":
        print("The loop is ended")
        break
    print(f"Hello {user_input}")