import datetime

class SmartHome:
    def __init__(self):
        self.rooms = {} 
        self.schedule = {}  

    def set_room_temperature(self, room_name, desired_temperature):
        self.rooms[room_name] = desired_temperature

    def display_rooms(self):
        print("Zonas de temperatura configuradas:")
        for room, temperature in self.rooms.items():
            print(f"{room}: {temperature}°C")

    def change_room_temperature(self, room_name, new_temperature):
        if room_name in self.rooms:
            self.rooms[room_name] = new_temperature
            print(f"Se ha ajustado la temperatura de la zona {room_name} a {new_temperature}°C.")
        else:
            print("La zona especificada no existe.")

    def schedule_temperature(self, room_name, start_hour, end_hour, temperature):
        if room_name not in self.schedule:
            self.schedule[room_name] = []
        self.schedule[room_name].append((start_hour, end_hour, temperature))
        print(f"Se ha programado el horario para la zona {room_name}: de {start_hour} a {end_hour}, {temperature}°C.")

    def auto_adjust_temperature(self):
        now = datetime.datetime.now()
        for room, schedules in self.schedule.items():
            for start_hour, end_hour, temperature in schedules:
                if start_hour <= now.hour < end_hour:
                    self.rooms[room] = temperature
                    print(f"Se ha ajustado automáticamente la temperatura de la zona {room} a {temperature}°C.")

    def monitor_temperature(self):
        for room, temperature in self.rooms.items():
            if room not in self.schedule:
                if temperature != 22:
                    self.rooms[room] = 22
                    print(f"Se ha ajustado automáticamente la temperatura de la zona {room} a 22°C.")

    def show_menu(self):
        print("\n--- Menú ---")
        print("1. Configurar zona de temperatura")
        print("2. Mostrar zonas configuradas")
        print("3. Ajustar temperatura de una zona")
        print("4. Programar horario")
        print("5. Ajustar temperatura automáticamente")
        print("6. Salir")

    def run(self):
        while True:
            self.show_menu()
            option = input("Selecciona una opción: ")

            if option == "1":
                room_name = input("Ingrese el nombre de la zona: ")
                desired_temperature = float(input("Ingrese la temperatura deseada (en °C): "))
                self.set_room_temperature(room_name, desired_temperature)
            elif option == "2":
                self.display_rooms()
            elif option == "3":
                room_name = input("Ingrese el nombre de la zona: ")
                new_temperature = float(input("Ingrese la nueva temperatura (en °C): "))
                self.change_room_temperature(room_name, new_temperature)
            elif option == "4":
                room_name = input("Ingrese el nombre de la zona: ")
                start_hour = int(input("Ingrese la hora de inicio (en formato de 24 horas): "))
                end_hour = int(input("Ingrese la hora de fin (en formato de 24 horas): "))
                temperature = float(input("Ingrese la temperatura (en °C): "))
                self.schedule_temperature(room_name, start_hour, end_hour, temperature)
            elif option == "5":
                self.auto_adjust_temperature()
                self.monitor_temperature()
            elif option == "6":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, selecciona una opción válida.")

home = SmartHome()
home.run()
