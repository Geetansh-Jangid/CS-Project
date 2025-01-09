import sys
import unit_converter
import chatbot
import image_generator
import graph_plotter
import csv_editor
import file_organiser
import password_generator
import file_organiser
import weather

def dashboard():
    print("\n=== Dashboard ===")
    print("1. Image Generator")
    print("2. Chatbot")
    print("3. Unit Converter")
    print("4. Graph Plotter")
    print("5. CSV Editor")
    print("6. File Organizer")
    print("7. Password Generator")
    print("8. Weather")
    print("9. Exit")

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

def unit_converter_menu():
    unit_converter.unit_converter()

def graph_plotter_menu():
    graph_plotter.graph_plotter()

def csv_editor_menu():
    csv_editor.csv_editor()

def file_organizer_menu():
    file_organiser.file_organizer()

def password_generator_menu():
    password_generator.password_generator()

def weather_menu():
    weather.weather()

def main():
    while True:
        dashboard()
        choice = input("\nEnter your choice: ")

        if choice == '1':
            image_generator_o()
        elif choice == '2':
            chatbot_menu()
        elif choice == '3':
            unit_converter_menu()
        elif choice == '4':
            graph_plotter_menu()
        elif choice == '5':
            csv_editor_menu()
            sys.exit()
        elif choice == '7':
            password_generator.password_generator()
        elif choice == '6':
            file_organizer.file_organizer()
        elif choice == '8':
            weather.weather_checker()
        elif choice == '9':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


