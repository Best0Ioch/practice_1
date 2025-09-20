from driver import Driver
from sedan import Sedan
from suv import SUV
from minivan import Minivan
from fleet import Fleet

def create_car() -> object:
    """Функція для створення авто з клавіатури"""
    car_type = input("Виберіть тип авто (sedan / suv / minivan): ").strip().lower()

    # Загальні параметри
    model = input("Введіть модель авто: ")
    speed = int(input("Введіть максимальну швидкість (км/год): "))
    seats = int(input("Введіть кількість місць: "))

    # Водій
    driver_name = input("Введіть ім'я водія: ")
    driving_experience = input("Введіть водійський стаж: ")
    driver = Driver(driver_name, driving_experience)

    # Конкретний тип авто
    if car_type == "sedan":
        trunk_volume = int(input("Введіть об'єм багажника (л): "))
        return Sedan(model, speed, seats, driver, trunk_volume)
    elif car_type == "suv":
        awd = input("Чи є повний привід? (так/ні): ").strip().lower() == "так"
        return SUV(model, speed, seats, driver, awd)
    elif car_type == "minivan":
        child_seat = input("Чи є дитяче крісло? (так/ні): ").strip().lower() == "так"
        return Minivan(model, speed, seats, driver, child_seat)
    else:
        print("Невідомий тип авто!")
        return None


if __name__ == "__main__":
    fleet_name = input("Введіть назву автопарку: ")
    fleet = Fleet(fleet_name)

    while True:
        print("\n--- МЕНЮ ---")
        print("1. Додати авто")
        print("2. Показати автопарк")
        print("3. Використати метод drive() ")
        print("4. Вихід")

        choice = input("Ваш вибір: ").strip()

        if choice == "1":
            car = create_car()
            if car:
                fleet.add_car(car)
                print("Авто додано!")

        elif choice == "2":
            fleet.show_fleet()

        elif choice == "3":
            if not fleet.cars:
                print("У автопарку немає жодної машини!")
                continue

            # показуємо список машин з індексами
            print("\nОберіть авто для поїздки:")
            for idx, car in enumerate(fleet.cars, start=1):
                print(f"{idx}. {car.model} ({car.__class__.__name__}) - водій {car.driver}")

            try:
                car_index = int(input("Введіть номер авто: ")) - 1
                if car_index < 0 or car_index >= len(fleet.cars):
                    print("❌ Невірний номер авто!")
                    continue
            except ValueError:
                print("❌ Потрібно ввести число!")
                continue

            car = fleet.cars[car_index]

            # Введення призначення
            user_input = input("Введіть дистанцію (число) або місто (текст): ")

            try:
                distance = int(user_input)
                car.drive(distance)
            except ValueError:
                car.drive(user_input)

        elif choice == "4":
            print("Вихід з програми...")
            break

        else:
            print("Невірний вибір! Спробуйте ще раз.")
