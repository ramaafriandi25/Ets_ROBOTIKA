import serial
import time

PORT = "COM3"
BAUDRATE = 115200

def main():
    try:
        with serial.Serial(PORT, BAUDRATE, timeout=1) as arduino:
            time.sleep(2)
            print("Terhubung dengan Arduino/iMCLab.")

            while True:
                command = input("Masukkan perintah (MAJU/MUNDUR/KIRI/KANAN/STOP/KELUAR): ").upper()

                if command == "KELUAR":
                    arduino.write(b"STOP\n")
                    break

                if command in ["MAJU", "MUNDUR", "KIRI", "KANAN", "STOP"]:
                    arduino.write((command + "\n").encode())
                    print("Perintah dikirim:", command)
                else:
                    print("Perintah tidak valid.")
    except serial.SerialException as error:
        print("Gagal terhubung:", error)

if __name__ == "__main__":
    main()
