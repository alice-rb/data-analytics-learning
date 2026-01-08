USE transactions;
-- 1.1 Creación tabla 'credit_card'
CREATE TABLE credit_card (
	id VARCHAR(20) NOT NULL,
    iban VARCHAR(50), 
    pan VARCHAR(50), 
    pin VARCHAR(4), 
    cvv VARCHAR(3),
    expiring_date VARCHAR(20),
    PRIMARY KEY (id)
    );

-- Modificación para adecuación en cantidad de carácteres de 'id' en 'credit_card'
ALTER TABLE transaction
MODIFY credit_card_id VARCHAR(20); 

-- Cargar los datos 
-- SOURCE datos_introduir_sprint3_credit.sql;

ALTER TABLE transaction
ADD CONSTRAINT fk_creditCard_id FOREIGN KEY (credit_card_id)
REFERENCES credit_card(id);

-- ----------------------------------------------------
-- CONSULTAS
-- ----------------------------------------------------
-- 1.2 Actualización de un registro en base a un id
UPDATE credit_card
SET iban = 'TR323456312213576817699999' -- nuevo iban
WHERE id='CcU-2938';

SELECT *
FROM credit_card
WHERE iban='TR301950312213576817638661'; -- iban previo

-- 1.3 Insertar nuevos datos en tabla 'transaction'
INSERT INTO company (id)
VALUES ('b-9999');
INSERT INTO credit_card (id)
VALUES ('CcU-9999');
INSERT INTO data_user (id)
VALUES ('9999');

INSERT INTO transaction (id,credit_card_id,
			company_id,user_id,lat,longitude,	
            amount,declined)
VALUES ('108B1D1D-5B23-A76C-55EF-C568E49A99DD', 'CcU-9999',
	'b-9999',9999,829.999,-117.999,111.11,0);

-- 1.4 Eliminar campo 'pan'
ALTER TABLE credit_card
DROP COLUMN pan;

SELECT pan -- no existe ese campo
FROM credit_card; 

-- 2.1 Eliminar registro de la tabla según id de transacción
DELETE FROM transaction 
WHERE id = '000447FE-B650-4DCF-85DE-C7ED0EE1CAAD';

SELECT * FROM transaction WHERE id='000447FE-B650-4DCF-85DE-C7ED0EE1CAAD'; -- no existe

-- 2.2 Creación de la vista "VistaMarketing"
CREATE VIEW vista_marketing AS ( 
	SELECT c.company_name as Empresa, c.phone as Telefono_contacto, 
			c.country as Pais, ROUND(AVG(t.amount),2) as Media_ventas
    FROM company c
    JOIN transaction t
    ON c.id = t.company_id
    GROUP BY c.id, Empresa,Telefono_contacto, Pais -- Buena práctica/optimizado es añadir el resto de campos en el GROUP BY
  #  ORDER BY Media_ventas DESC -- No poner ORDER BY en las vistas. Las vistas son solo el acceso a los datos, añadir eso consume recursos de manera innecesaria
);
SELECT * 
FROM vista_marketing;

-- 2.3 Filtra la vista VistaMarketing per a mostrar només les companyies que tenen el seu país de residència en "Germany"
SELECT Empresa 
FROM vista_marketing
WHERE Pais = 'Germany';

-- 3.1 Creación tabla data_user y explicación detallada del paso a paso

-- Usamos la BBDD de transactions, donde están el resto de nuestras tablas
USE transactions; 
-- Creamos la tabla de usuarios según SOURCE estructura datos user.sql
CREATE TABLE IF NOT EXISTS user ( 
	id CHAR(10) PRIMARY KEY,
	name VARCHAR(100),
	surname VARCHAR(100),
	phone VARCHAR(150),
	email VARCHAR(150),
	birth_date VARCHAR(100),
	country VARCHAR(150),
	city VARCHAR(150),
	postal_code VARCHAR(100),
	address VARCHAR(255)  
    );

-- Cambiamos el nombre de la tabla a 'data_user' para que coincida con el esquema
RENAME TABLE user to data_user; 
-- Cambiamos el tipo de dato del campo 'id' (de CHAR a INT), siendo este el tipo del campo 'user_id' en 'transaction'
ALTER TABLE data_user MODIFY id INT NOT NULL; 
-- Cambiamos el nombre del campo del 'email' para que coincida con el esquema
ALTER TABLE data_user CHANGE email personal_email VARCHAR(150); 

-- Para relacionar la tabla nueva con el resto, asignamos la FK 'user_id' de la tabla 'transaction' para unirla a la PK 'id' de la tabla 'data_user'
ALTER TABLE transaction 
ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) 
REFERENCES data_user(id) ON DELETE CASCADE ON UPDATE CASCADE;

-- Añadimos el campo 'fecha_actual' en la tabla 'credit_card'
ALTER TABLE credit_card 
ADD COLUMN fecha_actual DATE DEFAULT (CURRENT_DATE);
-- Cambiamos el tipo de dato del cvv a INT
ALTER TABLE credit_card
MODIFY cvv INT DEFAULT NULL;

-- Eliminamos el campo 'website' de la tabla 'company'
ALTER TABLE company
DROP COLUMN website;

-- Cargar los datos 
-- SOURCE datos introduir sprint3 user.sql;

-- 3.2 Creación de la vista "InformeTecnico" 

CREATE VIEW informe_tecnico AS 
	SELECT  t.id as Transaccion, u.name as Nombre, u.surname as Apellido, 
			cc.iban as IBAN, c.company_name as Empresa
    FROM transaction t
    JOIN data_user u ON t.user_id = u.id
    JOIN credit_card cc ON t.credit_card_id = cc.id
    JOIN company c ON t.company_id = c.id
    ORDER BY Transaccion DESC;

SELECT * 
FROM informe_tecnico;


