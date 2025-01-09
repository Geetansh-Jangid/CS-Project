import sys
import chatbot
import image_generator
import csv_editor
import file_organiser
import password_generator
import file_organiser

def dashboard():
    print("\n=== Dashboard ===")
    print("1. Image Generator")
    print("2. Chatbot")
    print("3. CSV Editor")
    print("4. File Organizer")
    print("5. Password Generator")
    print("6. Exit")

def image_generator_o():
    image_generator.image_generator()

def chatbot_menu():
    print("\n[Chatbot] - Type 'exit' to quit the chatbot.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            print("Exiting chatbot.")
            break
        response = chatbot.start_chatbot(user_input)
        print(f"Chatbot: {response}")

def csv_editor_menu():
    csv_editor.csv_editor()

def file_organizer_menu():
    file_organiser.file_organiser()

def password_generator_menu():
    password_generator.password_generator()

def main():
    while True:
        dashboard()
        choice = input("\nEnter your choice: ")

        if choice == '1':
            image_generator_o()
        elif choice == '2':
            chatbot_menu()
        elif choice == '3':
            csv_editor_menu()
            sys.exit()
        elif choice == '4':
            file_organizer_menu()
        elif choice == '5':
            password_generator.password_generator()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


