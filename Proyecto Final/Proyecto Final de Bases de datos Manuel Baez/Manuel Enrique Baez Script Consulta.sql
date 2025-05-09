SELECT 
    e.EstudianteID, 
    e.Nombre, 
    e.Apellido, 
    d.Nombre AS Departamento
FROM Estudiante e
JOIN Departamento d ON e.DepartamentoID = d.DepartamentoID;

SELECT 
    c.CursoID, 
    c.Nombre, 
    c.Creditos, 
    d.Nombre AS Departamento
FROM Curso c
JOIN Departamento d ON c.DepartamentoID = d.DepartamentoID;

SELECT 
    cl.ClaseID, 
    cu.Nombre AS Curso, 
    p.Nombre AS ProfesorNombre, 
    p.Apellido AS ProfesorApellido, 
    cl.Año, 
    cl.Semestre
FROM Clase cl
JOIN Curso cu ON cl.CursoID = cu.CursoID
JOIN Profesor p ON cl.ProfesorID = p.ProfesorID;

SELECT 
    i.InscripcionID,
    e.Nombre AS EstudianteNombre, 
    e.Apellido AS EstudianteApellido, 
    cl.ClaseID, 
    cu.Nombre AS Curso, 
    i.FechaInscripcion
FROM Inscripcion i
JOIN Estudiante e ON i.EstudianteID = e.EstudianteID
JOIN Clase cl ON i.ClaseID = cl.ClaseID
JOIN Curso cu ON cl.CursoID = cu.CursoID
WHERE cl.ClaseID = 1; 

SELECT 
    e.Nombre, 
    e.Apellido, 
    cu.Nombre AS Curso, 
    c.Nota
FROM Calificacion 
JOIN Inscripcion i ON c.InscripcionID = i.InscripcionID
JOIN Estudiante e ON i.EstudianteID = e.EstudianteID
JOIN Clase cl ON i.ClaseID = cl.ClaseID
JOIN Curso cu ON cl.CursoID = cu.CursoID
WHERE e.EstudianteID = 1;