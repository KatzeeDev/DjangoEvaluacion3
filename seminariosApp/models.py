from django.db import models
from django.utils import timezone
# Create your models here.

    

 
class Institucion(models.Model):
    id = models.AutoField(primary_key=True)
    institucion = models.CharField(max_length=200)

class Registro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    fecha_inscripcion = models.DateField()
    institucion_choices = [
        ("Universidad Catolica de Temuco", "Universidad Catolica de Temuco"),    
        ("Universidad de Chile", "Universidad de Chile"),    
        ("Universidad de Concepcion", "Universidad de Concepcion"),  
        ("Universidad de la frontera", "Universidad de la frontera"),    
        ("Universidad Santo Tomas", "Universidad Santo Tomas"),    
        ("Universidad Autonoma de Chile", "Universidad Autonoma de Chile"),    
        ("Inacap", "Inacap"),    
        ("AIEP", "AIEP"),
        ("Otro", "Otra Universidad"),
        ("Liceo", "Liceo"),
        ("Colegio", "Colegio"),
        
    ]
    institucion = models.CharField(max_length=50, choices=institucion_choices, default='Universidad Catolica')
    hora_inscripcion = models.TimeField()
    estado_choices = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO ASISTEN', 'No Asisten'),
    ]
    estado = models.CharField(max_length=20, choices=estado_choices, default='RESERVADO')
    observacion = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Verifica si la institución existe en el modelo Institucion
        institucion, created = Institucion.objects.get_or_create(institucion=self.institucion)
        if created:
            # Si la institución seleccionada no existe, la crea.
            institucion.save()
        # Establece la hora actual como hora de inscripción
        self.hora_inscripcion = timezone.now().time()
        # Luego, guarda la instancia del modelo Registro
        super(Registro, self).save(*args, **kwargs)
        
        
#TODO ================ Explicacion del codigo ================ 
# En mi caso decidi hacerlo de esa manera. Establecer ciertas opciones de las instituciones y cuando se creee una inscripcion con X institucion esta se creara en el sistema
# La hora es asignada automaticamente segun cuando se haga la inscripcion
