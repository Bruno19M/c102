import os
import shutil

from_dir = "C:/Users/manue/OneDrive/Documentos/Programacion"
to_dir = "C:/Users/manue/OneDrive/Documentos/Programacion/python/proyecto 102/Archivos_Documentos"

list_of_files = os.listdir(from_dir)
for file_name in list_of_files:
    file_extension = os.path.splitext(file_name)[1].lower()
    if file_extension:
        if file_extension in ['.txt', '.doc', '.docx', '.pdf']:
            file_path = os.path.join(from_dir, file_name)
ruta1 = from_dir+'/'+file_name
ruta2 = to_dir+'/'+"Archivos_Documentos"
ruta3 = to_dir+'/'+"Archivos_Documentos"+'/'+file_name

if os.path.exists(ruta2):
    print("Moviendo " + file_name + "...")
    shutil.move(ruta1,ruta3)
else:
    os.makedirs(ruta2)
    print("Moviendo " + file_name + "...")
    shutil.move(ruta1,ruta3)    
