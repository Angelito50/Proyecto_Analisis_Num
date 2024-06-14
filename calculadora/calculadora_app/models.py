from django.db import models
class tbl_usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    correo = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    fecha_inicio_sesion = models.DateField( auto_now=False, auto_now_add=False)
    
class tbl_Historial(models.Model):
    id_busqueda = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(tbl_usuarios, on_delete=models.RESTRICT)
    texto_busqueda = models.CharField(max_length=200)
    fecha_busqueda = models.DateField(auto_now=False, auto_now_add=False)

class tbl_Ecuaciones(models.Model):
    id_ecuacion = models.AutoField(primary_key=True) 
    ecuacion = models.CharField(max_length=200)
    ecuacion_simplificada = models.CharField(max_length=200, null=True)
    id_usuario = models.ForeignKey(tbl_usuarios, on_delete=models.RESTRICT)
    xi_ecuacion = models.CharField(max_length=200, null=True)
    fi_ecuacion = models.CharField(max_length=200, null=True)
    
class tbl_Soluciones(models.Model):
    id_solucion = models.AutoField(primary_key=True)
    id_ecuacion = models.ForeignKey(tbl_Ecuaciones, on_delete=models.RESTRICT)
    text_solucion = models.CharField(max_length=200)
    pasos = models.CharField(max_length=500)
    fecha_solucion = models.DateField(auto_now=False, auto_now_add=False)
    