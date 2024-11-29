import os
import time
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading

class FIFO:
    def __init__(self):
        self.elementos = []
    
    def agregar(self, elemento):
        self.elementos.append(elemento)
    
    def eliminar(self):
        if self.elementos:
            return self.elementos.pop(0)
        else:
            return None

class NanoxFileManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("NanoxNet_Corp - File Manager")
        self.root.geometry("600x600")
        self.root.configure(bg='black')
        
        self.style = ttk.Style()
        self.configurar_estilo()
        
        self.directorio_temporal = tk.StringVar(value="NanoxNet_corp")
        self.num_archivos = tk.IntVar(value=6)
        self.proceso_iniciado = False
        
        self.cola = FIFO()
        
        self.progreso = tk.DoubleVar()
        self.tiempo_inicio = None
        self.tiempo_estimado = tk.StringVar(value="Tiempo estimado: --:--")
        
        self.crear_widgets()
    
    def configurar_estilo(self):
        self.style.theme_use('clam')
        
        self.style.configure('TFrame', 
            background='black',
            borderwidth=0,
            relief='flat')
            
        self.style.configure('TLabel', 
            background='black', 
            foreground='#00FF00', 
            font=('Courier', 10, 'bold'))
            
        self.style.configure('TButton', 
            font=('Courier', 10, 'bold'), 
            padding=5,
            background='black',
            bordercolor='black',
            lightcolor='black',
            darkcolor='black')
            
        self.style.configure('TLabelframe', 
            background='black', 
            foreground='#00FF00', 
            font=('Courier', 10, 'bold'),
            borderwidth=0,
            relief='flat',
            bordercolor='#2e86c1')
            
        self.style.configure('Border.TLabelframe', 
            background='black', 
            foreground='#00FF00', 
            font=('Courier', 10, 'bold'),
            borderwidth=1,
            relief='solid',
            bordercolor='white')
            
        self.style.configure('TLabelframe.Label', 
            background='black', 
            foreground='#00FF00')
            
        self.style.configure('TEntry', 
            font=('Courier', 10), 
            background='black', 
            foreground='#00FF00',
            fieldbackground='black',
            bordercolor='black')

        self.style.configure(
            'Green.Horizontal.TProgressbar',
            troughcolor='black',
            background='#00FF00',
            darkcolor='blue',
            lightcolor='white',
            bordercolor='white'
        )

        self.style.configure('TSpinbox',
            fieldbackground='black',
            background='black',
            foreground='#00FF00',
            arrowcolor='white',
            bordercolor='black')

        self.style.configure('Info.TLabel',
            font=('Courier', 9),
            background='black',
            foreground='#00FF00')
        
        self.style.configure('Hacker.TButton',
            background='black',
            foreground='#00FF00',
            font=('Courier', 10, 'bold'),
            bordercolor='white')

        self.style.configure('Danger.TButton',
            background='black',
            foreground='red',
            font=('Courier', 10, 'bold'),
            bordercolor='white')
        
        self.style.map('Hacker.TButton',
            background=[('active', '#008000')],
            foreground=[('active', 'black')],
            bordercolor=[('active', 'white')])
            
        self.style.map('Danger.TButton',
            background=[('active', 'red')],
            foreground=[('active', 'black')],
            bordercolor=[('active', 'white')])

    def crear_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10 5 10 5")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        titulo = ttk.Label(main_frame, text="NanoxNet_Corp - File Manager", font=('Courier', 14, 'bold'), foreground='#00FF00')
        titulo.pack(pady=(0, 10))
        
        config_frame = ttk.LabelFrame(main_frame, text="Configuración")
        config_frame.pack(fill=tk.X, pady=5)
        
        dir_subframe = ttk.Frame(config_frame)
        dir_subframe.pack(fill=tk.X, padx=5, pady=2)
        ttk.Label(dir_subframe, text="Directorio:").pack(side=tk.LEFT)
        dir_entry = ttk.Entry(
            dir_subframe, 
            textvariable=self.directorio_temporal, 
            width=30,
            style='TEntry'
        )
        dir_entry.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
        num_subframe = ttk.Frame(config_frame)
        num_subframe.pack(fill=tk.X, padx=5, pady=2)
        ttk.Label(num_subframe, text="Archivos:").pack(side=tk.LEFT)
        num_entry = ttk.Spinbox(
            num_subframe, 
            from_=1, 
            to=20, 
            textvariable=self.num_archivos, 
            width=10,
            style='TSpinbox'
        )
        num_entry.pack(side=tk.LEFT, padx=5)
        
        cola_frame = ttk.LabelFrame(main_frame, text="Cola de Archivos", style='Border.TLabelframe')
        cola_frame.pack(fill=tk.X, pady=5)
        
        self.cola_listbox = tk.Listbox(
            cola_frame, 
            height=4, 
            font=('Courier', 10), 
            bg='black', 
            fg='#00FF00', 
            selectbackground='#008000', 
            selectforeground='black',
            borderwidth=1,
            highlightthickness=1,
            highlightcolor='white',
            highlightbackground='white'
        )
        self.cola_listbox.pack(fill=tk.X, padx=5, pady=5)
        
        log_frame = ttk.LabelFrame(main_frame, text="Log de Actividades", style='Border.TLabelframe')
        log_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.log_text = scrolledtext.ScrolledText(
            log_frame, 
            height=8, 
            wrap=tk.WORD, 
            font=('Courier', 10), 
            bg='black', 
            fg='#00FF00',
            borderwidth=1,
            highlightthickness=1,
            highlightcolor='white',
            highlightbackground='white'
        )
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.log_text.config(state=tk.DISABLED)
        
        progreso_frame = ttk.LabelFrame(main_frame, text="Progreso")
        progreso_frame.pack(fill=tk.X, pady=5)
           
        info_frame = ttk.Frame(progreso_frame)
        info_frame.pack(fill=tk.X, padx=5)
        
        self.archivos_label = ttk.Label(
            info_frame, 
            text="Procesados: 0/0",
            style='Info.TLabel'
        )
        self.archivos_label.pack(side=tk.LEFT, padx=5)
        
        self.tiempo_label = ttk.Label(
            info_frame,
            textvariable=self.tiempo_estimado,
            style='Info.TLabel'
        )
        self.tiempo_label.pack(side=tk.RIGHT, padx=5)
                    
        self.barra_progreso = ttk.Progressbar(
            progreso_frame,
            variable=self.progreso,
            maximum=100,
            mode='determinate',
            length=200,
            style='Green.Horizontal.TProgressbar'
        )
        self.barra_progreso.pack(fill=tk.X, padx=5, pady=5)
        
        self.porcentaje_label = ttk.Label(
            progreso_frame, 
            text="0%",
            style='Info.TLabel'
        )
        self.porcentaje_label.pack()
        
        # Frame de botones
        btn_frame = ttk.Frame(main_frame)
        btn_frame.pack(pady=5)
        
        self.inicio_btn = ttk.Button(
            btn_frame, 
            text="Iniciar", 
            command=self.iniciar_proceso, 
            style='Hacker.TButton'
        )
        self.inicio_btn.pack(side=tk.LEFT, padx=3)
        
        salir_btn = ttk.Button(
            btn_frame, 
            text="Salir", 
            command=self.root.quit, 
            style='Danger.TButton'
        )
        salir_btn.pack(side=tk.LEFT, padx=3)
        
        # Firma
        firma = ttk.Label(
            self.root, 
            text="By_NanoEspinoza", 
            font=('Courier', 8, 'italic'), 
            foreground='#00FF00', 
            anchor="se"
        )
        firma.place(relx=1.0, rely=1.0, x=-5, y=-5, anchor="se")

    def calcular_tiempo_estimado(self, porcentaje):
        if not self.tiempo_inicio:
            self.tiempo_inicio = time.time()
            return "Calculando..."
            
        tiempo_transcurrido = time.time() - self.tiempo_inicio
        if porcentaje > 0:
            tiempo_total_estimado = (tiempo_transcurrido * 100) / porcentaje
            tiempo_restante = tiempo_total_estimado - tiempo_transcurrido
            minutos = int(tiempo_restante // 60)
            segundos = int(tiempo_restante % 60)
            return f"Tiempo restante: {minutos:02d}:{segundos:02d}"
        return "Calculando..."

    def actualizar_progreso(self):
        total_archivos = self.num_archivos.get()
        archivos_restantes = len(self.cola.elementos)
        archivos_procesados = total_archivos - archivos_restantes
        porcentaje = (archivos_procesados / total_archivos) * 100
        
        self.progreso.set(porcentaje)
        self.porcentaje_label.config(text=f"{int(porcentaje)}%")
        
        self.archivos_label.config(
            text=f"Procesados: {archivos_procesados}/{total_archivos}"
        )
        
        tiempo_est = self.calcular_tiempo_estimado(porcentaje)
        self.tiempo_estimado.set(tiempo_est)
        
        if porcentaje < 33:
            color = '#FF0000'
        elif porcentaje < 66:
            color = '#FFFF00'
        else:
            color = '#00FF00'
            
        self.style.configure(
            'Green.Horizontal.TProgressbar',
            background=color,
            darkcolor='white',
            lightcolor='white',
            bordercolor='white'
        )
    def log(self, mensaje):
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, mensaje + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)

    def iniciar_proceso(self):
        if self.proceso_iniciado:
            messagebox.showinfo("Información", "El proceso ya está en marcha.")
            return
        
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete('1.0', tk.END)
        self.log_text.config(state=tk.DISABLED)
        
        self.cola_listbox.delete(0, tk.END)
        
        
        self.progreso.set(0)
        self.porcentaje_label.config(text="0%")
        self.tiempo_inicio = None
        self.tiempo_estimado.set("Tiempo estimado: --:--")
        self.archivos_label.config(text=f"Procesados: 0/{self.num_archivos.get()}")
        
        directorio = self.directorio_temporal.get()
        num_archivos = self.num_archivos.get()
        
        try:
            os.makedirs(directorio, exist_ok=True)
            self.log(f"Creando directorio: {directorio}")
            
            for i in range(num_archivos):
                nombre_archivo = f"Nanito_{i+1}.txt"
                ruta_archivo = os.path.join(directorio, nombre_archivo)
                with open(ruta_archivo, 'w') as f:
                    f.write(f"Contenido del archivo {nombre_archivo}")
                self.cola.agregar(nombre_archivo)
                self.cola_listbox.insert(tk.END, nombre_archivo)
                self.log(f"Archivo creado: {nombre_archivo}")
            
            self.proceso_iniciado = True
            threading.Thread(target=self.eliminar_archivos, daemon=True).start()
            self.log("Proceso iniciado exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.log(f"Error: {e}")
    
    def eliminar_archivos(self):
        try:
            while self.proceso_iniciado and self.cola.elementos:
                archivo = self.cola.elementos[0]
                ruta_archivo = os.path.join(self.directorio_temporal.get(), archivo)
                try:
                    os.remove(ruta_archivo)
                    eliminado = self.cola.eliminar()
                    self.root.after(0, self.log, f"Archivo eliminado: {archivo}")
                    self.root.after(0, self.actualizar_listbox, archivo)
                    self.root.after(0, self.actualizar_progreso)
                except Exception as e:
                    self.root.after(0, self.log, f"Error al eliminar {archivo}: {e}")
                time.sleep(5)
            
            directorio = self.directorio_temporal.get()
            try:
                os.rmdir(directorio)
                self.root.after(0, self.log, f"Directorio eliminado: {directorio}")
            except OSError as e:
                self.root.after(0, self.log, f"No se pudo eliminar el directorio {directorio}: {e}")
            
            self.root.after(0, self.finalizar_proceso)
        except Exception as e:
            self.root.after(0, self.log, f"Error en proceso de eliminación: {e}")
            self.root.after(0, self.finalizar_proceso)
    
    def actualizar_listbox(self, archivo):
        index = self.cola_listbox.get(0, tk.END).index(archivo)
        self.cola_listbox.delete(index)
    
    def finalizar_proceso(self):
        self.proceso_iniciado = False
        self.log("Todos los archivos procesados.")

def main():
    root = tk.Tk()
    app = NanoxFileManagerGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()