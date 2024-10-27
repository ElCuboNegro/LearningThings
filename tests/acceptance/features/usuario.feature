# features/usuario.feature

Feature: Gestión de Usuarios

  Scenario: Asignar un username automáticamente
    Given que tengo un usuario sin username
    When guardo el usuario
    Then el username debe ser NO NULL
    AND el username debe ser igual al ID del usuario
    AND el user_first_name debe ser null
    AND el user_last_name debe ser null
    AND el genero del usuario debe ser null
    AND la foto de perfil debe ser null
    AND la fecha de creación debe ser la fecha actual
    AND la fecha de modificación debe ser la fecha actual
    AND la fecha de eliminación debe ser null
    AND el estado civil debe ser null
    AND la fecha de nacimiento debe ser null
    AND el tipo de 16 personalidades A debe ser null
    AND el tipo de 16 personalidades B debe ser null
    AND el tipo de 16 personalidades C debe ser null
    AND el tipo de 16 personalidades D debe ser null
    AND la fecha del último evento debe ser null
    AND el "spontime activo" debe ser false
    AND el "actividades spontime activo" debe ser un array vacío
    AND la reputación debe ser 0
    AND los gustos de actividades deben ser un array vacío


  Scenario: Crear un nuevo usuario
    Given que tengo un usuario con el nombre "Juan" y el género "masculino"
    When guardo el usuario
    Then el usuario debe ser creado con el nombre "Juan"
    AND el genero debe ser "masculino"

  Scenario: Crear un nuevo usuario con un nombre parecido a un uuid
    Given que tengo un usuario con un nombre parecido a un uuid
    When guardo el usuario
    Then debe rechazarse el guardado
    

