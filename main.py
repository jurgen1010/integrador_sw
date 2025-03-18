import datetime;
import decimal;
import pyodbc;
"""
	varInteger: int = 253; # int(253);
	varLong: int = 2350006657; # int(2350006657);
	varFloat: float = 10.5; # float(10.2);
	varDecimal: decimal = 15.6;
	varString: str = "Test"; # str("Valor 2");
	varDate: datetime = datetime.datetime.now();
	varBool: bool = True; # bool(True);
"""

# DTO, ENTIDAD...
class Habitacion:
    id: int = 0
    numero: int = 0
    precioPorNoche: float = 0.0
    estado: str = None
    capacidad: int = 0
    tipo: str = None
    descripcion: str = None

    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    def GetNumero(self) -> int:
        return self.numero
    def SetNumero(self, value: int) -> None:
        self.numero = value

    def GetPrecioPorNoche(self) -> float:
        return self.precioPorNoche
    def SetPrecioPorNoche(self, value: float) -> None:
        self.precioPorNoche = value

    def GetEstado(self) -> str:
        return self.estado
    def SetEstado(self, value: str) -> None:
        self.estado = value

    def GetCapacidad(self) -> int:
        return self.capacidad
    def SetCapacidad(self, value: int) -> None:
        self.capacidad = value

    def GetTipo(self) -> str:
        return self.tipo
    def SetTipo(self, value: str) -> None:
        self.tipo = value

    def GetDescripcion(self) -> str:
        return self.descripcion
    def SetDescripcion(self, value: str) -> None:
        self.descripcion = value

class Huesped:
    id: int = 0
    nombre: str = None
    apellido: str = None
    email: str = None
    telefono: str = None
    habitacion_id: int = 0

    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    def GetNombre(self) -> str:
        return self.nombre
    def SetNombre(self, value: str) -> None:
        self.nombre = value

    def GetApellido(self) -> str:
        return self.apellido
    def SetApellido(self, value: str) -> None:
        self.apellido = value

    def GetEmail(self) -> str:
        return self.email
    def SetEmail(self, value: str) -> None:
        self.email = value

    def GetTelefono(self) -> str:
        return self.telefono
    def SetTelefono(self, value: str) -> None:
        self.telefono = value

    def GetHabitacionId(self) -> int:
        return self.habitacion_id
    def SetHabitacionId(self, value: int) -> None:
        self.habitacion_id = value

# REPOSITORIO
class Repositorio:
    strConnection: str = """
        Driver={MySQL ODBC 9.2 Unicode Driver};
        Server=localhost;
        Database=db_hotel;
        PORT=3306;
        user=user_ptyhon;
        password=Clas3s1Nt2024_!"""

    def ConsultarHabitaciones(self) -> None:
        conexion = pyodbc.connect(self.strConnection)

        # Consulta para la tabla habitaciones
        consulta_habitaciones: str = """SELECT * FROM habitaciones"""
        cursor = conexion.cursor()
        cursor.execute(consulta_habitaciones)

        lista_habitaciones: list = []
        for elemento in cursor:
            habitacion: Habitacion = Habitacion()
            habitacion.SetId(elemento[0])
            habitacion.SetNumero(elemento[1])
            habitacion.SetPrecioPorNoche(elemento[2])
            habitacion.SetEstado(elemento[3])
            habitacion.SetCapacidad(elemento[4])
            habitacion.SetTipo(elemento[5])
            habitacion.SetDescripcion(elemento[6])
            lista_habitaciones.append(habitacion)

        # Consulta para la tabla huespedes
        consulta_huespedes: str = """SELECT * FROM huespedes"""
        cursor.execute(consulta_huespedes)

        lista_huespedes: list = []
        for elemento in cursor:
            huesped: Huesped = Huesped()
            huesped.SetId(elemento[0])
            huesped.SetNombre(elemento[1])
            huesped.SetApellido(elemento[2])
            huesped.SetEmail(elemento[3])
            huesped.SetTelefono(elemento[4])
            huesped.SetHabitacionId(elemento[5])
            lista_huespedes.append(huesped)

        cursor.close()
        conexion.close()

        # Imprimir resultados
        print("Habitaciones:")
        for habitacion in lista_habitaciones:
            print(f"ID: {habitacion.GetId()}, Numero: {habitacion.GetNumero()}, Precio: {habitacion.GetPrecioPorNoche()}, Estado: {habitacion.GetEstado()}, Capacidad: {habitacion.GetCapacidad()}, Tipo: {habitacion.GetTipo()}, Descripcion: {habitacion.GetDescripcion()}")

        print("\nHuespedes:")
        for huesped in lista_huespedes:
            print(f"ID: {huesped.GetId()}, Nombre: {huesped.GetNombre()}, Apellido: {huesped.GetApellido()}, Email: {huesped.GetEmail()}, Telefono: {huesped.GetTelefono()}, Habitacion ID: {huesped.GetHabitacionId()}")

    def IngresarReserva(self, huesped: Huesped) -> None:
        conexion = pyodbc.connect(self.strConnection)
        cursor = conexion.cursor()
        consulta = """INSERT INTO huespedes (nombre, apellido, email, telefono, habitacion_id) 
                      VALUES (?, ?, ?, ?, ?)"""
        cursor.execute(consulta, (huesped.GetNombre(), huesped.GetApellido(), huesped.GetEmail(), huesped.GetTelefono(), huesped.GetHabitacionId()))
        conexion.commit()
        cursor.close()
        conexion.close()

repositorio = Repositorio();
repositorio.ConsultarHabitaciones();


nuevo_huesped = Huesped()
nuevo_huesped.SetNombre('Jurgen')
nuevo_huesped.SetApellido('Perez')
nuevo_huesped.SetEmail('jurgen.perez@example.com')
nuevo_huesped.SetTelefono('3185570524')
nuevo_huesped.SetHabitacionId(1) 
repositorio.IngresarReserva(nuevo_huesped)

