#Developer: Universidad
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import scrolledtext
from tkinter import messagebox
import os
import time
import subprocess


v0=Tk()
v0.title("Control de puertos firewall")
v0.geometry("700x500+0+0")

text_gral =font.Font(family="Helvetica", size=12)

def Addports():
                v1=Toplevel()
                v1.title("Agregar Puertos")
                v1.geometry("500x200+300+200")

                def clean():
                        ports.set("")

                def save():
                        p=str(ports.get())
                        enc="#!/bin/bash"
                        con1="sudo ufw allow"
                        tab=" "
                        cadena=(str(con1)+''+str(tab)+''+str(p))
                        os.system("sudo touch /home/klopz/seguridad/addports.sh")
                        os.system("sudo chmod -R 777 /home/klopz/seguridad/addports.sh")
                        pf=open("/home/klopz/seguridad/addports.sh", "w")
                        pf.write(enc)
                        pf.write("\n")
                        pf.write(cadena)
                        pf.write("\n")
                        pf.close()

                        time.sleep(0.1)

                        os.system("sudo /./home/klopz/seguridad/addports.sh")
                        messagebox.showinfo("info", message="Puerto Agregado con exito")

                text_v1 = font.Font(family="Helvetica", size = 12)
                label_port = Label(v1, text ="Ingrese Numero de Puerto :", font= text_v1).place(x=10, y=80)
                global ports
                ports = StringVar()
                txt_port=Entry(v1,textvariable = ports, width = 20).place(x=210, y=80)

                btn_save = Button(v1, text="Save", bg="green", fg="white", command = save).place(x=390, y=80)

                v1.mainloop()

def listport():
                print("Activando")
                os.system("sudo /./home/klopz/seguridad/listport.sh > /home/klopz/seguridad/listport.txt")
                valor=subprocess.check_output("cat /home/klopz/seguridad/listport.txt",shell=True)
                area1=scrolledtext.ScrolledText(v0, width=80, height = 10)
                area1.place(x=10, y=80)
                area1.insert(END, valor)
listport()

def deleteport():
                op=radio.get()
                if (op==1):
                            action="allow"
                            p=str(puertodel.get())
                            enc="#!/bin/bash"
                            con1="sudo ufw delete"
                            tab=" "
                            cadena=(str(con1)+' '+str(tab)+' '+str(action)+' '+str(tab)+' '+str(p))
                            print(cadena)
                            os.system("sudo touch /home/klopz/seguridad/deleteport.sh")
                            os.system("sudo chmod -R 777 /home/klopz/seguridad/deleteport.sh")
                            pf=open("/home/klopz/seguridad/deleteport.sh", "w")
                            pf.write(enc)
                            pf.write("\n")
                            pf.write(cadena)
                            pf.write("\n")
                            pf.close()

                            time.sleep(0.1)

                            os.system("sudo /./home/klopz/seguridad/deleteport.sh &")
                            messagebox.showinfo("info", message ="Puerto Eliminado con exito", parent=v0)
                            
def sitios_web():
                v2=Toplevel()
                v2.title("Sitos Web")
                v2.geometry("700x400+200+200")
                text_sitio=font.Font(family="Helvetica",size=14)

                def clean_tiempo():
                    horai.set('')
                    minini.set('')
                    horaf.set('')
                    minf.set('')
                
                def Tiempo_sitio_uth():

                                    def save_tiempo_uth():
                                        print("---Temporizador----")
                                        hi=str(horai.get())
                                        mi=str(minini.get())
                                        hf=str(horaf.get())
                                        mf=str(minf.get())

                                        dia="*"
                                        mes="*"
                                        ism="*"
                                        user="root"
                                        path1="/home/klopz/seguridad/bloquear_uth.sh"
                                        path2="/home/klopz/seguridad/desbloquear_uth.sh"
                                        tab=" "

                                        cadena1=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ism)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path1))
                                        cadena2=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(ism)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path2))

                                        os.system("sudo chmod -R 777 /etc/cron.d/task_uth_enable")
                                        os.system("sudo chmod -R 777 /etc/cron.d/task_uth_disable")

                                        pf1=open("/etc/cron.d/task_uth_enable", "w")
                                        pf1.write(cadena1)
                                        pf1.write("\n")
                                        pf1.close()

                                        pf1=open("/etc/cron.d/task_uth_disable", "w")
                                        pf1.write(cadena2)
                                        pf1.write("\n")
                                        pf1.close()

                                        #pausa

                                        time.sleep(0.1)

                                        #revertir permisos segun necesita el usuario root

                                        os.system("sudo chmod -R 755 /etc/cron.d/task_uth_enable")
                                        os.system("sudo chmod -R 755 /etc/cron.d/task_uth_disable")

                                        # Reiniciar el servicio cron

                                        os.system("sudo /etc/init.d/cron restart")
                                        clean_tiempo()
                                        
                                        messagebox.showinfo("INFO",message="Tiempo Programado con exito!")
                                        
                                    print("Temporizador...")
                                    label_horai=Label(v2,text="Hora Inicial",font=text_sitio).place(x=10, y=250)
                                    label_minini=Label(v2,text="Minuto Inicial",font=text_sitio).place(x=10, y=280)
                                    label_horaf=Label(v2,text="Hora Final",font=text_sitio).place(x=10, y=310)
                                    labl_minif=Label(v2,text="Minuto Final",font=text_sitio).place(x=10, y=340)

                                    global horai,minini,horaf,minf
                                    horai=StringVar()
                                    minini=StringVar()
                                    horaf=StringVar()
                                    minf=StringVar()

                                    txt_hrai=Entry(v2, textvariable=horai,width=20).place(x=130, y=250)
                                    txt_minini=Entry(v2, textvariable=minini,width=20).place(x=130, y=280)
                                    txt_horaf=Entry(v2, textvariable=horaf,width=20).place(x=130, y=310)
                                    txt_minf=Entry(v2, textvariable=minf,width=20).place(x=130, y=340)

                                    btn_save_tiempo=Button(v2,text="Save", command=save_tiempo_uth).place(x=350, y=300)
                                    
                def Block_sitio_web():
                                    print("Bloqueo y desbloqueo de sitios web")
                                    cks3=str(check_sitio3.get())
                                    if (cks3=="1"):
                                        os.system("sudo /./home/klopz/seguridad/bloquear2.sh &")
                                        messagebox.showinfo("INFO", message="Sitio Bloqueado", parent=v2)
                                        label_permitido=Label(v2,text="Bloqueado", bg="black",fg="red",font=text_sitio).place(x=220,y=180)

                                    if (cks3=="0"):
                                        os.system("sudo /./home/klopz/seguridad/desbloquear2.sh &")
                                        messagebox.showinfo("INFO", message="Sitio desbloqueado", parent=v2)
                                        label_permitido=Label(v2,text="Bloqueado", bg="green",fg="red",font=text_sitio).place(x=220,y=180)
                                    
                
                #Variables
                global check_sitio1,  check_sitio2, check_sitio3, sitioweb
                check_sitio1 = StringVar()
                check_sitio2 = StringVar()
                check_sitio3 = StringVar()
                sitioweb = StringVar()

                #check box de sitios web
                ck1=ttk.Checkbutton(v2, text="www.facebook.com", variable=check_sitio1, command = Block_sitio_web).place(x=50,y=100)
                ck2=ttk.Checkbutton(v2, text="www.diez.hn", variable=check_sitio2, command = Block_sitio_web)
                ck2.place(x=50,y=140)
                ck3=ttk.Checkbutton(v2, text="www.laprensa.hn", variable=check_sitio3, command = Block_sitio_web).place(x=50,y=180)
                
                #Labels
                label_sitio=Label(v2,text="URL sitio web: ", font=text_sitio).place(x=20, y=40)
                
                # Cajas de texto
                txt_sitioweb = Entry(v2, textvariable=sitioweb, width=50).place(x=150, y=40)
                
                #Botones de la ventana 2 - Sitios web
                btn_tiempo=Button(v2,text="Tiempo", bg="brown", fg="white", command=Tiempo_sitio_uth).place(x=250, y=180)

                v2.mainloop()
                
# Botones de la ventana 0
btn_add=Button(v0, text="Add_Ports",bg="green",fg="white", command=Addports).place(x=100, y= 50)
btn_list=Button(v0, text="List port", command=listport).place(x=10, y=50)
btn_sitios=Button(v0, text="sitios_Web", bg="orange",fg="white", command=sitios_web).place(x=10,y=340)


label_port = Label(v0, text = "Puerto: ", font = text_gral).place(x=300, y=50)

global puertodel
puertodel = StringVar()
txt_del = Entry(v0, textvariable= puertodel, width=10).place(x=380, y=50)
global radio

radio=IntVar()
r1=ttk.Radiobutton(v0,text="allow",variable=radio,value=1, command=deleteport).place(x=500, y=50)
r2=ttk.Radiobutton(v0,text="deny", variable=radio, value=2, command=deleteport).place(x=590, y=50)
label_t2=Label(v0, text="Eliminar", font=text_gral).place(x=550, y=20)

v0.mainloop()

