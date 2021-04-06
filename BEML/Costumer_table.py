create table
transferor_Master(
    ID
int,
PAN
VARCHAR(10),
Name
TEXT,
category
char(1),
PAN_Status
char(1),
Plot_flat_no
varchar(255),
Aline1
varchar(255),
Aline2
varchar(255),
Aline3
varchar(255),
City
varchar(255),
State
varchar(255),
Pincode
int,
Email
varchar(255),
Cell
int
);

insert
into
transferor_Master
values(1, 'AAJPC0081L', 'Prestige Estates Limited', 'I', 'A', '32/17', '3rd cross',
       'bhuvaneshwari nagar', 'BSK 3rd stage', 'Bengaluru', 'Karnataka', 560091, 'abc@yahoo.com', 12345678);

insert
into
transferor_Master
values(2, 'BQLPK6187B', 'Century builders', 'I', 'A', 'No. 7', '7th cross',
       'CSI Compound', 'off mission road', 'Bengaluru', 'Karnataka', 560037, 'def@yahoo.com', 87654321);

create
table
transferee_Master(
    ID
int,
PAN
varchar(10),
DOB
date,
Name
TEXT,
Category
char(1),
PAN_Status
char(1),
Plot_flat_no
varchar(255),
Aline1
varchar(255),
Aline2
varchar(255),
Aline3
varchar(255),
City
varchar(255),
State
varchar(255),
Pincode
int,
Email
varchar(255),
Cell
int
);

insert
into
transferee_Master
values(1, 'AZQPK9981G', '1981-06-01', 'John K', 'I', 'A', '#3456', 'Nagarabhavi main road', '', 'vijayanagara',
       'Bengaluru', 'Karnataka', 560078, 'mno@yahoo.com', 23456789);
insert
into
transferee_Master
values(2, 'AOCPJ6868S', '1994-09-01', 'Rishab Jain', 'I', 'A', '5689', 'Rishab Jain', '', 'Sampangirama Nagar',
       'Bengaluru', 'Karnataka', 560037, 'pqr@yahoo.com', 98765432);

create
table
property_master(
    ID
int,
transferor_id
int,
Transferee_ID
int,
Project_Name
text,
Project_code
varchar(255),
property_type
char(10),
Property_Value
Bigint,
Plot_flat_no
varchar(255),
Aline1
varchar(255),
Aline2
varchar(255),
Aline3
varchar(255),
City
varchar(255),
State
varchar(255),
Pincode
int,
Single_seller
char(1),
Single_Buyer
char(1),
Date_of_Agreement
DATE
);

insert
into
property_master
values(1, 1, 1, 'Prestige Tech Park', 'Prestige-0001', 'Land', 900000000, '#269/2', 'Kasturiba Nagar', '',
       'Mysore Road', 'Bengaluru', 'Karnataka', 560026, 'S', 'S', '2000-01-01');
insert
into
property_master
values(2, 1, 1, 'Prestige Tech Park', 'Prestige-0001', 'Aprtment', 100000000, '#270/2', 'Kasturiba Nagar', '',
       'Mysore Road', 'Bengaluru', 'Karnataka', 560026, 'S', 'S', '2000-01-01');

insert
into
property_master
values(3, 1, 2, 'Sky height apartments', 'Prestige-0002', 'Apartments', 500000000, '#280/72', 'Four square chamber', '',
       'M.G. Road', 'Bengaluru', 'Karnataka', 560085, 'S', 'S', '2001-02-01');
insert
into
property_master
values(4, 1, 2, 'Sky height apartments', 'Prestige-0002', 'Apartments', 4900000, '#280/73', 'Four square chamber', '',
       'M.G. Road', 'Bengaluru', 'Karnataka', 560085, 'S', 'S', '2001-02-01');

create
table
payment_Master(
    Payment_ID
int,
Property_ID
int,
Transferor_ID
int,
Transferee_ID
int,
payment_type
char(20),
Residential_Status
char(10),
Amount
bigint,
TDS_Prcnt
int,
Date_of_payment
date,
Date_of_tax_deduction
date,
mode_of_payment
char(20)
);

insert
into
payment_Master
values(1, 1, 1, 1, 'Initial Deposit', 'Resident', 10000000, 1, '2005-01-01', '2005-01-01', 'check');
insert
into
payment_Master
values(2, 2, 1, 1, 'Initialment 1', 'Resident', 100000, 1, '2005-01-01', '2005-01-01', 'check');

insert
into
payment_Master
values(3, 3, 1, 2, 'Initial Deposit', 'Resident', 800000, 1, '2006-01-01', '2006-01-01', 'check');
insert
into
payment_Master
values(4, 4, 1, 2, 'Initialment 1', 'Resident', 10000000, 1, '2006-01-01', '2006-01-01', 'check');
insert
into
payment_Master
values(5, 4, 1, 2, 'Initialment 2', 'Resident', 10000000, 1, '2006-02-01', '2006-02-01', 'check');

drop
function if exists
F_Max_Transferor_ID;
DELIMITER $$

CREATE
FUNCTION
F_Max_Transferor_ID()
RETURNS
int
DETERMINISTIC
BEGIN
DECLARE
transferor_id
int;

SELECT
max(id)
into
transferor_id
from transferor_Master;

--
return the
customer
level
RETURN(transferor_id + 1);
END$$
DELIMITER;

DELIMITER $$

CREATE
FUNCTION
F_TaxApplicable(
    Property_value
bigint
)
RETURNS
VARCHAR(20)
DETERMINISTIC
BEGIN
DECLARE
TaxApplicable
VARCHAR(20);

IF
Property_value > 5000000
THEN
SET
TaxApplicable = '002';
ELSE
SET
TaxApplicable = '001';
END
IF;
--
return the
customer
level
RETURN(TaxApplicable);
END$$
DELIMITER;

DELIMITER $$

CREATE
FUNCTION
F_Minor_Head_Code()
RETURNS
int
DETERMINISTIC
BEGIN
DECLARE
minor_head_code
int;

SET
minor_head_code = 800;
RETURN(minor_head_code);
END$$
DELIMITER;

DROP
FUNCTION
F_Fin_Year;

DELIMITER $$

CREATE
FUNCTION
F_Fin_Year(payment_date
date)
RETURNS
varchar(10)
DETERMINISTIC
BEGIN
DECLARE
fin_year
varchar(10);
DECLARE
cur_year
int;
DECLARE
next_year
int;
SET
cur_year = DATE_FORMAT(payment_date, '%Y');
SET
next_year = cur_year + 1;
SET
fin_year = CONCAT(cur_year, '-', next_year);
RETURN(fin_year);
END$$
DELIMITER;

DROP
FUNCTION
IF
EXISTS
F_Assement_Year;

DELIMITER $$

CREATE
FUNCTION
F_Assement_Year(payment_date
date)
RETURNS
varchar(10)
DETERMINISTIC
BEGIN
DECLARE
assessment_year
varchar(10);
DECLARE
cur_year
int;
DECLARE
next_year
int;
SET
cur_year = DATE_FORMAT(payment_date, '%Y') + 1;
SET
next_year = cur_year + 1;
SET
assessment_year = CONCAT(cur_year, '-', next_year);
RETURN(assessment_year);
END$$
DELIMITER;

drop
view if exists
v_transaction_record;

create
view
v_transaction_record
as
select
F_TaxApplicable(prm.Property_Value) as tax_applicable,
F_Minor_Head_Code() as Minor_Head_Code,
F_Fin_Year(pym.Date_of_payment) as Fin_year,
F_Assement_Year(pym.Date_of_payment) as Assemet_Year,
pym.Amount
amount_paid, pym.TDS_Prcnt, pym.mode_of_payment,
pym.date_of_payment, pym.Date_of_tax_deduction,
tranfr_m.Name
Transferor_Name, tranfr_m.PAN
Transferor_PAN, tranfr_m.PAN_Status
Transferor_PAN_Status,
tranfr_m.Plot_flat_no
Transferor_Plot_flat_no, tranfr_m.Aline1
Transferor_Aline1,
tranfr_m.Aline2
Transferor_Aline2, tranfr_m.Aline3
Transferor_Aline3,
tranfr_m.City
Transferor_City, tranfr_m.State
Transferor_State,
tranfr_m.Pincode
Transferor_PinCode, tranfr_m.Email
Transferor_Email, tranfr_m.Cell
Transferor_Cell,
tranfe_m.Name
Transferee_Name, tranfe_m.PAN
Transferee_PAN, tranfe_m.PAN_Status
Transferee_PAN_Status,
tranfe_m.Plot_flat_no
Transferee_Plot_flat_no, tranfe_m.Aline1
Transferee_Aline1,
tranfe_m.Aline2
Transferee_Aline2, tranfe_m.Aline3
Transferee_Aline3,
tranfe_m.City
Transferee_City, tranfe_m.State
Transferee_State,
tranfe_m.Pincode
Transferee_PinCode, tranfe_m.Email
Transferee_Email, tranfe_m.Cell
Transferee_Cell,
prm.Project_Name
Transferred_Name, prm.Plot_flat_no
Transferrred_Plot_flat_no, prm.Aline1
Transferred_Aline1,
prm.Aline2
Transferred_Aline2, prm.Aline3
Transferred_Aline3,
prm.City
Transferred_City, prm.State
Transferred_State,
prm.Pincode
Transferred_PinCode, prm.Single_Buyer, prm.Single_seller, prm.property_type,
prm.Property_Value, prm.Date_of_Agreement
from payment_Master pym, property_master

prm, transferor_Master
tranfr_m, transferee_Master
tranfe_m
where
pym.Property_ID = prm.ID
and pym.Transferor_ID = tranfr_m.ID
and pym.Transferee_ID = tranfe_m.ID;

select *
from v_transaction_record;
