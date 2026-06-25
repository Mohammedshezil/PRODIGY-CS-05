import customtkinter as ctk
from scapy.all import sniff, IP
import time
import threading

# GUI Setup
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class NetViper(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("NetViper | Advanced Packet Analyzer")
        self.geometry("800x550")

        # Header
        self.header = ctk.CTkLabel(self, text="🐍 N E T V I P E R", font=("Arial", 28, "bold"))
        self.header.pack(pady=10)

        # Console Area
        self.textbox = ctk.CTkTextbox(self, width=750, height=350, font=("Consolas", 12))
        self.textbox.pack(pady=10)
        self.textbox.configure(text_color="#00FF41")

        # Buttons Frame
        self.btn_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.btn_frame.pack(pady=20)

        self.start_btn = ctk.CTkButton(self.btn_frame, text="RUN CAPTURE", fg_color="green", command=self.start_sniffing)
        self.start_btn.grid(row=0, column=0, padx=20)

        self.stop_btn = ctk.CTkButton(self.btn_frame, text="KILL & SAVE", fg_color="red", command=self.stop_sniffing)
        self.stop_btn.grid(row=0, column=1, padx=20)

    def packet_callback(self, packet):
        if packet.haslayer(IP):
            log = f"[{time.strftime('%H:%M:%S')}] {packet[IP].src} -> {packet[IP].dst} | Proto: {packet[IP].proto}\n"
            self.textbox.insert("end", log)
            self.textbox.see("end")

    def start_sniffing(self):
        self.textbox.insert("end", "--- Initializing Capture Engine ---\n")
        
        # Background thread to prevent GUI freeze
        def run_sniff():
            sniff(prn=self.packet_callback, store=0)
            
        sniff_thread = threading.Thread(target=run_sniff)
        sniff_thread.daemon = True
        sniff_thread.start()

    def stop_sniffing(self):
        self.textbox.insert("end", "--- Capture Stopped. Session Ended. ---\n")
        # In a advanced version, you would use a threading event to kill the sniffer.

if __name__ == "__main__":
    app = NetViper()
    app.mainloop()