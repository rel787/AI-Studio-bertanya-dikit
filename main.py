import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Inisialisasi model Gemini
model = genai.GenerativeModel("gemini-1.5-flash")

# Menyimpan history sebagai list
history = []

def format_history(hist):
    """Gabungkan history jadi 1 prompt panjang"""
    return "\n".join(hist)

def main():
    print("🤖 Gemini AI Chat Bot")
    print("Ketik 'exit' untuk keluar\n")

    while True:
        user_input = input("Anda: ")
        if user_input.lower() == "exit":
            print("Terima kasih! Sampai jumpa!")
            break

        try:
            # Tambahkan pertanyaan ke history
            history.append(f"User: {user_input}")

            # Gabungkan history dan kirim ke model
            prompt = format_history(history)
            response = model.generate_content(prompt)

            # Tambahkan respon ke history
            ai_reply = response.text.strip()
            history.append(f"Gemini: {ai_reply}")

            # Tampilkan jawaban
            print(f"Gemini: {ai_reply}\n")

        except Exception as e:
            print(f"Terjadi error: {e}\n")

if __name__ == "__main__":
    main()
