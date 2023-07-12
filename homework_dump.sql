PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE countries(
country_id varchar(2) primary key  not null,
country_name varchar(40) not null,
region_id integer(2) not null);
INSERT INTO countries VALUES('country_id','country_name','region_id');
INSERT INTO countries VALUES('AR','Argentina',2);
INSERT INTO countries VALUES('AU','Australia',3);
INSERT INTO countries VALUES('BE','Belgium',1);
INSERT INTO countries VALUES('BR','Brazil',2);
INSERT INTO countries VALUES('CA','Canada',2);
INSERT INTO countries VALUES('CH','Switzerland',1);
INSERT INTO countries VALUES('CN','China',3);
INSERT INTO countries VALUES('DE','Germany',1);
INSERT INTO countries VALUES('DK','Denmark',1);
INSERT INTO countries VALUES('EG','Egypt',4);
INSERT INTO countries VALUES('FR','France',1);
INSERT INTO countries VALUES('HK','HongKong',3);
INSERT INTO countries VALUES('IL','Israel',4);
INSERT INTO countries VALUES('IN','India',3);
INSERT INTO countries VALUES('IT','Italy',1);
INSERT INTO countries VALUES('JP','Japan',3);
INSERT INTO countries VALUES('KW','Kuwait',4);
INSERT INTO countries VALUES('MX','Mexico',2);
INSERT INTO countries VALUES('NG','Nigeria',4);
INSERT INTO countries VALUES('NL','Netherlands',1);
INSERT INTO countries VALUES('SG','Singapore',3);
INSERT INTO countries VALUES('UK','United Kingdom',1);
INSERT INTO countries VALUES('US','United States of America',2);
INSERT INTO countries VALUES('ZM','Zambia',4);
INSERT INTO countries VALUES('ZW','Zimbabwe',4);
CREATE TABLE regions(
region_id integer(2) primary key not null,
region_name varchar(25) not null);
INSERT INTO regions VALUES('REGION_ID','REGION_NAME');
INSERT INTO regions VALUES(1,'Europe');
INSERT INTO regions VALUES(2,'Americas');
INSERT INTO regions VALUES(3,'Asia');
INSERT INTO regions VALUES(4,'Middle East and Africa');
INSERT INTO regions VALUES(999,'MONE_999');
CREATE TABLE locations(
location_id integer(4) primary key not null,
street_address varchar(25) not null,
postal_code varchar(12),
city varchar(30) not null,
state_province varchar(12),
country_id varchar(2));
INSERT INTO locations VALUES(1000,'1297 Via Cola di Rie','989','Roma','','IT');
INSERT INTO locations VALUES(1100,'93091 Calle della Testa','10934','Venice','','IT');
INSERT INTO locations VALUES(1200,'2017 Shinjuku-ku','1689','Tokyo','Tokyo Prefecture','JP');
INSERT INTO locations VALUES(1300,'9450 Kamiya-cho','6823','Hiroshima','','JP');
INSERT INTO locations VALUES(1400,'2014 Jabberwocky Rd','26192','Southlake','Texas','US');
INSERT INTO locations VALUES(1500,'2011 Interiors Blvd','99236','South San Francisco','California','US');
INSERT INTO locations VALUES(1600,'2007 Zagora St','50090','South Brunswick','New Jersey','US');
INSERT INTO locations VALUES(1700,'2004 Charade Rd','98199','Seattle','Washington','US');
INSERT INTO locations VALUES(1800,'147 Spadina Ave','M5V 2L7','Toronto','Ontario','CA');
INSERT INTO locations VALUES(1900,'6092 Boxwood St','YSW 9T2','Whitehorse','Yukon','CA');
INSERT INTO locations VALUES(2000,'40-5-12 Laogianggen','190518','Beijing','','CN');
INSERT INTO locations VALUES(2100,'1298 Vileparle (E)','490231','Bombay','Maharashtra','IN');
INSERT INTO locations VALUES(2200,'12-98 Victoria Street','2901','Sydney','New South Wales','AU');
INSERT INTO locations VALUES(2300,'198 Clementi North','540198','Singapore','','SG');
INSERT INTO locations VALUES(2400,'8204 Arthur St','','London','','UK');
INSERT INTO locations VALUES(2500,'Magdalen Centre, The Oxford Science Park','OX9 9ZB','Oxford','Oxford','UK');
INSERT INTO locations VALUES(2600,'9702 Chester Road','9629850293','Stretford','Manchester','UK');
INSERT INTO locations VALUES(2700,'Schwanthalerstr. 7031','80925','Munich','Bavaria','DE');
INSERT INTO locations VALUES(2800,'Rua Frei Caneca 1360','01307-002','Sao Paulo','Sao Paulo','BR');
INSERT INTO locations VALUES(2900,'20 Rue des Corps-Saints','1730','Geneva','Geneve','CH');
INSERT INTO locations VALUES(3000,'Murtenstrasse 921','3095','Bern','BE','CH');
INSERT INTO locations VALUES(3100,'Pieter Breughelstraat 837','3029SK','Utrecht','Utrecht','NL');
INSERT INTO locations VALUES(3200,'Mariano Escobedo 9991','11932','Mexico City','Distrito Federal,','MX');
CREATE TABLE departments(
department_id integer(3) primary key not null,
depart_name varchar(20) not null,
manager_id integer(3) not null,
location_id integer(4));
INSERT INTO departments VALUES(10,'Administration',200,1700);
INSERT INTO departments VALUES(20,'Marketing',201,1800);
INSERT INTO departments VALUES(30,'Purchasing',114,1700);
INSERT INTO departments VALUES(40,'Human Resources',203,2400);
INSERT INTO departments VALUES(50,'Shipping',121,1500);
INSERT INTO departments VALUES(60,'IT',103,1400);
INSERT INTO departments VALUES(70,'Public Relations',204,2700);
INSERT INTO departments VALUES(80,'Sales',145,2500);
INSERT INTO departments VALUES(90,'Executive',100,1700);
INSERT INTO departments VALUES(100,'Finance',108,1700);
INSERT INTO departments VALUES(110,'Accounting',205,1700);
INSERT INTO departments VALUES(120,'Treasury','',1700);
INSERT INTO departments VALUES(130,'Corporate Tax','',1700);
INSERT INTO departments VALUES(140,'Control And Credit','',1700);
INSERT INTO departments VALUES(150,'Shareholder Services','',1700);
INSERT INTO departments VALUES(160,'Benefits','',1700);
INSERT INTO departments VALUES(170,'Manufacturing','',1700);
INSERT INTO departments VALUES(180,'Construction','',1700);
INSERT INTO departments VALUES(190,'Contracting','',1700);
INSERT INTO departments VALUES(200,'Operations','',1700);
INSERT INTO departments VALUES(210,'IT Support','',1700);
INSERT INTO departments VALUES(220,'NOC','',1700);
INSERT INTO departments VALUES(230,'IT Helpdesk','',1700);
INSERT INTO departments VALUES(240,'Government Sales','',1700);
INSERT INTO departments VALUES(250,'Retail Sales','',1700);
INSERT INTO departments VALUES(260,'Recruiting','',1700);
INSERT INTO departments VALUES(270,'Payroll','',1700);
CREATE TABLE jobs(
job_id varchar(10) primary key not null,
job_title varchar(25) not null,
min_salary decimal,
max_salary decimal);
INSERT INTO jobs VALUES('job_id','job_title','min_salary','max_salary');
INSERT INTO jobs VALUES('AD_PRES','President',20000,40000);
INSERT INTO jobs VALUES('AD_VP','Administration Vice President',15000,30000);
INSERT INTO jobs VALUES('AD_ASST','Administration Assistant',3000,6000);
INSERT INTO jobs VALUES('FI_MGR','Finance Manager',8200,16000);
INSERT INTO jobs VALUES('FI_ACCOUNT','Accountant',4200,9000);
INSERT INTO jobs VALUES('AC_MGR','Accounting Manager',8200,16000);
INSERT INTO jobs VALUES('AC_ACCOUNT','Public Accountant',4200,9000);
INSERT INTO jobs VALUES('SA_MAN','Sales Manager',10000,20000);
INSERT INTO jobs VALUES('SA_REP','Sales Representative',6000,12000);
INSERT INTO jobs VALUES('PU_MAN','Purchasing Manager',8000,15000);
INSERT INTO jobs VALUES('PU_CLERK','Purchasing Clerk',2500,5500);
INSERT INTO jobs VALUES('ST_MAN','Stock Manager',5500,8500);
INSERT INTO jobs VALUES('ST_CLERK','Stock Clerk',2000,5000);
INSERT INTO jobs VALUES('SH_CLERK','Shipping Clerk',2500,5500);
INSERT INTO jobs VALUES('IT_PROG','Programmer',4000,10000);
INSERT INTO jobs VALUES('MK_MAN','Marketing Manager',9000,15000);
INSERT INTO jobs VALUES('MK_REP','Marketing Representative',4000,9000);
INSERT INTO jobs VALUES('HR_REP','Human Resources Representative',4000,9000);
INSERT INTO jobs VALUES('PR_REP','Public Relations Representative',4500,10500);
CREATE TABLE employees(
employee_id integer(3) primary key not null,
first_name varchar(20),
last_name varchar(25),
email varchar(25),
phone_number varchar(20),
hire_date date,
job_id varchar(10) not null,
salary decimal,
commission_pct number,
manager_id integer(3),
department_id integer(3), Avg_Salary NUMERIC);
INSERT INTO employees VALUES(100,'Steven','King','SKING','515.123.4567','1987-06-17','AD_PRES',24000,0,0,90,NULL);
INSERT INTO employees VALUES(101,'Neena','Kochhar','NKOCHHAR','515.123.4568','1987-06-18','AD_VP',17000,0,100,90,NULL);
INSERT INTO employees VALUES(102,'Lex','De Haan','LDEHAAN','515.123.4569','1987-06-19','AD_VP',17000,0,100,90,NULL);
INSERT INTO employees VALUES(103,'Alexander','Hunold','AHUNOLD','590.423.4567','1987-06-20','IT_PROG',9000,0,102,60,NULL);
INSERT INTO employees VALUES(104,'Bruce','Ernst','BERNST','590.423.4568','1987-06-21','IT_PROG',6000,0,103,60,NULL);
INSERT INTO employees VALUES(105,'David','Austin','DAUSTIN','590.423.4569','1987-06-22','IT_PROG',4800,0,103,60,NULL);
INSERT INTO employees VALUES(106,'Valli','Pataballa','VPATABAL','590.423.4560','1987-06-23','IT_PROG',4800,0,103,60,NULL);
INSERT INTO employees VALUES(107,'Diana','Lorentz','DLORENTZ','590.423.5567','1987-06-24','IT_PROG',4200,0,103,60,NULL);
INSERT INTO employees VALUES(108,'Nancy','Greenberg','NGREENBE','515.124.4569','1987-06-25','FI_MGR',12000,0,101,100,NULL);
INSERT INTO employees VALUES(109,'Daniel','Faviet','DFAVIET','515.124.4169','1987-06-26','FI_ACCOUNT',9000,0,108,100,NULL);
INSERT INTO employees VALUES(110,'John','Chen','JCHEN','515.124.4269','1987-06-27','FI_ACCOUNT',8200,0,108,100,NULL);
INSERT INTO employees VALUES(111,'Ismael','Sciarra','ISCIARRA','515.124.4369','1987-06-28','FI_ACCOUNT',7700,0,108,100,NULL);
INSERT INTO employees VALUES(112,'Jose Manuel','Urman','JMURMAN','515.124.4469','1987-06-29','FI_ACCOUNT',7800,0,108,100,NULL);
INSERT INTO employees VALUES(113,'Luis','Popp','LPOPP','515.124.4567','1987-06-30','FI_ACCOUNT',6900,0,108,100,NULL);
INSERT INTO employees VALUES(114,'Den','Raphaely','DRAPHEAL','515.127.4561','1987-07-01','PU_MAN',11000,0,100,30,NULL);
INSERT INTO employees VALUES(115,'Alexander','Khoo','AKHOO','515.127.4562','1987-07-02','PU_CLERK',3100,0,114,30,NULL);
INSERT INTO employees VALUES(116,'Shelli','Baida','SBAIDA','515.127.4563','1987-07-03','PU_CLERK',2900,0,114,30,NULL);
INSERT INTO employees VALUES(117,'Sigal','Tobias','STOBIAS','515.127.4564','1987-07-04','PU_CLERK',2800,0,114,30,NULL);
INSERT INTO employees VALUES(118,'Guy','Himuro','GHIMURO','515.127.4565','1987-07-05','PU_CLERK',2600,0,114,30,NULL);
INSERT INTO employees VALUES(119,'Karen','Colmenares','KCOLMENA','515.127.4566','1987-07-06','PU_CLERK',2500,0,114,30,NULL);
INSERT INTO employees VALUES(120,'Matthew','Weiss','MWEISS','650.123.1234','1987-07-07','ST_MAN',8000,0,100,50,NULL);
INSERT INTO employees VALUES(121,'Adam','Fripp','AFRIPP','650.123.2234','1987-07-08','ST_MAN',8200,0,100,50,NULL);
INSERT INTO employees VALUES(122,'Payam','Kaufling','PKAUFLIN','650.123.3234','1987-07-09','ST_MAN',7900,0,100,50,NULL);
INSERT INTO employees VALUES(123,'Shanta','Vollman','SVOLLMAN','650.123.4234','1987-07-10','ST_MAN',6500,0,100,50,NULL);
INSERT INTO employees VALUES(124,'Kevin','Mourgos','KMOURGOS','650.123.5234','1987-07-11','ST_MAN',5800,0,100,50,NULL);
INSERT INTO employees VALUES(125,'Julia','Nayer','JNAYER','650.124.1214','1987-07-12','ST_CLERK',3200,0,120,50,NULL);
INSERT INTO employees VALUES(126,'Irene','Mikkilineni','IMIKKILI','650.124.1224','1987-07-13','ST_CLERK',2700,0,120,50,NULL);
INSERT INTO employees VALUES(127,'James','Landry','JLANDRY','650.124.1334','1987-07-14','ST_CLERK',2400,0,120,50,NULL);
INSERT INTO employees VALUES(128,'Steven','Markle','SMARKLE','650.124.1434','1987-07-15','ST_CLERK',2200,0,120,50,NULL);
INSERT INTO employees VALUES(129,'Laura','Bissot','LBISSOT','650.124.5234','1987-07-16','ST_CLERK',3300,0,121,50,NULL);
INSERT INTO employees VALUES(130,'Mozhe','Atkinson','MATKINSO','650.124.6234','1987-07-17','ST_CLERK',2800,0,121,50,NULL);
INSERT INTO employees VALUES(131,'James','Marlow','JAMRLOW','650.124.7234','1987-07-18','ST_CLERK',2500,0,121,50,NULL);
INSERT INTO employees VALUES(132,'TJ','Olson','TJOLSON','650.124.8234','1987-07-19','ST_CLERK',2100,0,121,50,NULL);
INSERT INTO employees VALUES(133,'Jason','Mallin','JMALLIN','650.127.1934','1987-07-20','ST_CLERK',3300,0,122,50,NULL);
INSERT INTO employees VALUES(134,'Michael','Rogers','MROGERS','650.127.1834','1987-07-21','ST_CLERK',2900,0,122,50,NULL);
INSERT INTO employees VALUES(135,'Ki','Gee','KGEE','650.127.1734','1987-07-22','ST_CLERK',2400,0,122,50,NULL);
INSERT INTO employees VALUES(136,'Hazel','Philtanker','HPHILTAN','650.127.1634','1987-07-23','ST_CLERK',2200,0,122,50,NULL);
INSERT INTO employees VALUES(137,'Renske','Ladwig','RLADWIG','650.121.1234','1987-07-24','ST_CLERK',3600,0,123,50,NULL);
INSERT INTO employees VALUES(138,'Stephen','Stiles','SSTILES','650.121.2034','1987-07-25','ST_CLERK',3200,0,123,50,NULL);
INSERT INTO employees VALUES(139,'John','Seo','JSEO','650.121.2019','1987-07-26','ST_CLERK',2700,0,123,50,NULL);
INSERT INTO employees VALUES(140,'Joshua','Patel','JPATEL','650.121.1834','1987-07-27','ST_CLERK',2500,0,123,50,NULL);
INSERT INTO employees VALUES(141,'Trenna','Rajs','TRAJS','650.121.8009','1987-07-28','ST_CLERK',3500,0,124,50,NULL);
INSERT INTO employees VALUES(142,'Curtis','Davies','CDAVIES','650.121.2994','1987-07-29','ST_CLERK',3100,0,124,50,NULL);
INSERT INTO employees VALUES(143,'Randall','Matos','RMATOS','650.121.2874','1987-07-30','ST_CLERK',2600,0,124,50,NULL);
INSERT INTO employees VALUES(144,'Peter','Vargas','PVARGAS','650.121.2004','1987-07-31','ST_CLERK',2500,0,124,50,NULL);
INSERT INTO employees VALUES(145,'John','Russell','JRUSSEL','011.44.1344.429268','1987-08-01','SA_MAN',14000,0.4000000000000000222,100,80,NULL);
INSERT INTO employees VALUES(146,'Karen','Partners','KPARTNER','011.44.1344.467268','1987-08-02','SA_MAN',13500,0.29999999999999998889,100,80,NULL);
INSERT INTO employees VALUES(147,'Alberto','Errazuriz','AERRAZUR','011.44.1344.429278','1987-08-03','SA_MAN',12000,0.29999999999999998889,100,80,NULL);
INSERT INTO employees VALUES(148,'Gerald','Cambrault','GCAMBRAU','011.44.1344.619268','1987-08-04','SA_MAN',11000,0.29999999999999998889,100,80,NULL);
INSERT INTO employees VALUES(149,'Eleni','Zlotkey','EZLOTKEY','011.44.1344.429018','1987-08-05','SA_MAN',10500,0.2000000000000000111,100,80,NULL);
INSERT INTO employees VALUES(150,'Peter','Tucker','PTUCKER','011.44.1344.129268','1987-08-06','SA_REP',10000,0.29999999999999998889,145,80,NULL);
INSERT INTO employees VALUES(151,'David','Bernstein','DBERNSTE','011.44.1344.345268','1987-08-07','SA_REP',9500,0.25,145,80,NULL);
INSERT INTO employees VALUES(152,'Peter','Hall','PHALL','011.44.1344.478968','1987-08-08','SA_REP',9000,0.25,145,80,NULL);
INSERT INTO employees VALUES(153,'Christopher','Olsen','COLSEN','011.44.1344.498718','1987-08-09','SA_REP',8000,0.2000000000000000111,145,80,NULL);
INSERT INTO employees VALUES(154,'Nanette','Cambrault','NCAMBRAU','011.44.1344.987668','1987-08-10','SA_REP',7500,0.2000000000000000111,145,80,NULL);
INSERT INTO employees VALUES(155,'Oliver','Tuvault','OTUVAULT','011.44.1344.486508','1987-08-11','SA_REP',7000,0.14999999999999999444,145,80,NULL);
INSERT INTO employees VALUES(156,'Janette','King','JKING','011.44.1345.429268','1987-08-12','SA_REP',10000,0.34999999999999997779,146,80,NULL);
INSERT INTO employees VALUES(157,'Patrick','Sully','PSULLY','011.44.1345.929268','1987-08-13','SA_REP',9500,0.34999999999999997779,146,80,NULL);
INSERT INTO employees VALUES(158,'Allan','McEwen','AMCEWEN','011.44.1345.829268','1987-08-14','SA_REP',9000,0.34999999999999997779,146,80,NULL);
INSERT INTO employees VALUES(159,'Lindsey','Smith','LSMITH','011.44.1345.729268','1987-08-15','SA_REP',8000,0.29999999999999998889,146,80,NULL);
INSERT INTO employees VALUES(160,'Louise','Doran','LDORAN','011.44.1345.629268','1987-08-16','SA_REP',7500,0.29999999999999998889,146,80,NULL);
INSERT INTO employees VALUES(161,'Sarath','Sewall','SSEWALL','011.44.1345.529268','1987-08-17','SA_REP',7000,0.25,146,80,NULL);
INSERT INTO employees VALUES(162,'Clara','Vishney','CVISHNEY','011.44.1346.129268','1987-08-18','SA_REP',10500,0.25,147,80,NULL);
INSERT INTO employees VALUES(163,'Danielle','Greene','DGREENE','011.44.1346.229268','1987-08-19','SA_REP',9500,0.14999999999999999444,147,80,NULL);
INSERT INTO employees VALUES(164,'Mattea','Marvins','MMARVINS','011.44.1346.329268','1987-08-20','SA_REP',7200,0.10000000000000000555,147,80,NULL);
INSERT INTO employees VALUES(165,'David','Lee','DLEE','011.44.1346.529268','1987-08-21','SA_REP',6800,0.10000000000000000555,147,80,NULL);
INSERT INTO employees VALUES(166,'Sundar','Ande','SANDE','011.44.1346.629268','1987-08-22','SA_REP',6400,0.10000000000000000555,147,80,NULL);
INSERT INTO employees VALUES(167,'Amit','Banda','ABANDA','011.44.1346.729268','1987-08-23','SA_REP',6200,0.10000000000000000555,147,80,NULL);
INSERT INTO employees VALUES(168,'Lisa','Ozer','LOZER','011.44.1343.929268','1987-08-24','SA_REP',11500,0.25,148,80,NULL);
INSERT INTO employees VALUES(169,'Harrison','Bloom','HBLOOM','011.44.1343.829268','1987-08-25','SA_REP',10000,0.2000000000000000111,148,80,NULL);
INSERT INTO employees VALUES(170,'Tayler','Fox','TFOX','011.44.1343.729268','1987-08-26','SA_REP',9600,0.2000000000000000111,148,80,NULL);
INSERT INTO employees VALUES(171,'William','Smith','WSMITH','011.44.1343.629268','1987-08-27','SA_REP',7400,0.14999999999999999444,148,80,NULL);
INSERT INTO employees VALUES(172,'Elizabeth','Bates','EBATES','011.44.1343.529268','1987-08-28','SA_REP',7300,0.14999999999999999444,148,80,NULL);
INSERT INTO employees VALUES(173,'Sundita','Kumar','SKUMAR','011.44.1343.329268','1987-08-29','SA_REP',6100,0.10000000000000000555,148,80,NULL);
INSERT INTO employees VALUES(174,'Ellen','Abel','EABEL','011.44.1644.429267','1987-08-30','SA_REP',11000,0.29999999999999998889,149,80,NULL);
INSERT INTO employees VALUES(175,'Alyssa','Hutton','AHUTTON','011.44.1644.429266','1987-08-31','SA_REP',8800,0.25,149,80,NULL);
INSERT INTO employees VALUES(176,'Jonathon','Taylor','JTAYLOR','011.44.1644.429265','1987-09-01','SA_REP',8600,0.2000000000000000111,149,80,NULL);
INSERT INTO employees VALUES(177,'Jack','Livingston','JLIVINGS','011.44.1644.429264','1987-09-02','SA_REP',8400,0.2000000000000000111,149,80,NULL);
INSERT INTO employees VALUES(178,'Kimberely','Grant','KGRANT','011.44.1644.429263','1987-09-03','SA_REP',7000,0.14999999999999999444,149,0,NULL);
INSERT INTO employees VALUES(179,'Charles','Johnson','CJOHNSON','011.44.1644.429262','1987-09-04','SA_REP',6200,0.10000000000000000555,149,80,NULL);
INSERT INTO employees VALUES(180,'Winston','Taylor','WTAYLOR','650.507.9876','1987-09-05','SH_CLERK',3200,0,120,50,NULL);
INSERT INTO employees VALUES(181,'Jean','Fleaur','JFLEAUR','650.507.9877','1987-09-06','SH_CLERK',3100,0,120,50,NULL);
INSERT INTO employees VALUES(182,'Martha','Sullivan','MSULLIVA','650.507.9878','1987-09-07','SH_CLERK',2500,0,120,50,NULL);
INSERT INTO employees VALUES(183,'Girard','Geoni','GGEONI','650.507.9879','1987-09-08','SH_CLERK',2800,0,120,50,NULL);
INSERT INTO employees VALUES(184,'Nandita','Sarchand','NSARCHAN','650.509.1876','1987-09-09','SH_CLERK',4200,0,121,50,NULL);
INSERT INTO employees VALUES(185,'Alexis','Bull','ABULL','650.509.2876','1987-09-10','SH_CLERK',4100,0,121,50,NULL);
INSERT INTO employees VALUES(186,'Julia','Dellinger','JDELLING','650.509.3876','1987-09-11','SH_CLERK',3400,0,121,50,NULL);
INSERT INTO employees VALUES(187,'Anthony','Cabrio','ACABRIO','650.509.4876','1987-09-12','SH_CLERK',3000,0,121,50,NULL);
INSERT INTO employees VALUES(188,'Kelly','Chung','KCHUNG','650.505.1876','1987-09-13','SH_CLERK',3800,0,122,50,NULL);
INSERT INTO employees VALUES(189,'Jennifer','Dilly','JDILLY','650.505.2876','1987-09-14','SH_CLERK',3600,0,122,50,NULL);
INSERT INTO employees VALUES(190,'Timothy','Gates','TGATES','650.505.3876','1987-09-15','SH_CLERK',2900,0,122,50,NULL);
INSERT INTO employees VALUES(191,'Randall','Perkins','RPERKINS','650.505.4876','1987-09-16','SH_CLERK',2500,0,122,50,NULL);
INSERT INTO employees VALUES(192,'Sarah','Bell','SBELL','650.501.1876','1987-09-17','SH_CLERK',4000,0,123,50,NULL);
INSERT INTO employees VALUES(193,'Britney','Everett','BEVERETT','650.501.2876','1987-09-18','SH_CLERK',3900,0,123,50,NULL);
INSERT INTO employees VALUES(194,'Samuel','McCain','SMCCAIN','650.501.3876','1987-09-19','SH_CLERK',3200,0,123,50,NULL);
INSERT INTO employees VALUES(195,'Vance','Jones','VJONES','650.501.4876','1987-09-20','SH_CLERK',2800,0,123,50,NULL);
INSERT INTO employees VALUES(196,'Alana','Walsh','AWALSH','650.507.9811','1987-09-21','SH_CLERK',3100,0,124,50,NULL);
INSERT INTO employees VALUES(197,'Kevin','Feeney','KFEENEY','650.507.9822','1987-09-22','SH_CLERK',3000,0,124,50,NULL);
INSERT INTO employees VALUES(198,'Donald','OConnell','DOCONNEL','650.507.9833','1987-09-23','SH_CLERK',2600,0,124,50,NULL);
INSERT INTO employees VALUES(199,'Douglas','Grant','DGRANT','650.507.9844','1987-09-24','SH_CLERK',2600,0,124,50,NULL);
INSERT INTO employees VALUES(200,'Jennifer','Whalen','JWHALEN','515.123.4444','1987-09-25','AD_ASST',4400,0,101,10,NULL);
INSERT INTO employees VALUES(201,'Michael','Hartstein','MHARTSTE','515.123.5555','1987-09-26','MK_MAN',13000,0,100,20,NULL);
INSERT INTO employees VALUES(202,'Pat','Fay','PFAY','603.123.6666','1987-09-27','MK_REP',6000,0,201,20,NULL);
INSERT INTO employees VALUES(203,'Susan','Mavris','SMAVRIS','515.123.7777','1987-09-28','HR_REP',6500,0,101,40,NULL);
INSERT INTO employees VALUES(204,'Hermann','Baer','HBAER','515.123.8888','1987-09-29','PR_REP',10000,0,101,70,NULL);
INSERT INTO employees VALUES(205,'Shelley','Higgins','SHIGGINS','515.123.8080','1987-09-30','AC_MGR',12000,1,101,110,NULL);
INSERT INTO employees VALUES(206,'William','Gietz','WGIETZ','515.123.8181','1987-10-01','AC_ACCOUNT',8300,1,205,110,NULL);
CREATE TABLE department(
  "department_id" TEXT,
  "department_name" TEXT,
  "manager_id" TEXT,
  "location_id" TEXT
);
INSERT INTO department VALUES('10','Administration','200','1700');
INSERT INTO department VALUES('20','Marketing','201','1800');
INSERT INTO department VALUES('30','Purchasing','114','1700');
INSERT INTO department VALUES('40','Human Resources','203','2400');
INSERT INTO department VALUES('50','Shipping','121','1500');
INSERT INTO department VALUES('60','IT','103','1400');
INSERT INTO department VALUES('70','Public Relations','204','2700');
INSERT INTO department VALUES('80','Sales','145','2500');
INSERT INTO department VALUES('90','Executive','100','1700');
INSERT INTO department VALUES('100','Finance','108','1700');
INSERT INTO department VALUES('110','Accounting','205','1700');
INSERT INTO department VALUES('120','Treasury','','1700');
INSERT INTO department VALUES('130','Corporate Tax','','1700');
INSERT INTO department VALUES('140','Control And Credit','','1700');
INSERT INTO department VALUES('150','Shareholder Services','','1700');
INSERT INTO department VALUES('160','Benefits','','1700');
INSERT INTO department VALUES('170','Manufacturing','','1700');
INSERT INTO department VALUES('180','Construction','','1700');
INSERT INTO department VALUES('190','Contracting','','1700');
INSERT INTO department VALUES('200','Operations','','1700');
INSERT INTO department VALUES('210','IT Support','','1700');
INSERT INTO department VALUES('220','NOC','','1700');
INSERT INTO department VALUES('230','IT Helpdesk','','1700');
INSERT INTO department VALUES('240','Government Sales','','1700');
INSERT INTO department VALUES('250','Retail Sales','','1700');
INSERT INTO department VALUES('260','Recruiting','','1700');
INSERT INTO department VALUES('270','Payroll','','1700');
CREATE TABLE job_history(
employee_id integer(3) not null,
start_date date not null,
end_date date not null,
job_id varchar(10) not null,
department_id integer(3) not null);
INSERT INTO job_history VALUES('employee_id','start_date','end_date`','job_id','department_id');
INSERT INTO job_history VALUES(102,'1993-01-13','1998-07-24','IT_PROG',60);
INSERT INTO job_history VALUES(101,'1989-09-21','1993-10-27','AC_ACCOUNT',110);
INSERT INTO job_history VALUES(101,'1993-10-28','1997-03-15','AC_MGR',110);
INSERT INTO job_history VALUES(201,'1996-02-17','1999-12-19','MK_REP',20);
INSERT INTO job_history VALUES(114,'1998-03-24','1999-12-31','ST_CLERK',50);
INSERT INTO job_history VALUES(122,'1999-01-01','1999-12-31','ST_CLERK',50);
INSERT INTO job_history VALUES(200,'1987-09-17','1993-06-17','AD_ASST',90);
INSERT INTO job_history VALUES(176,'1998-03-24','1998-12-31','SA_REP',80);
INSERT INTO job_history VALUES(176,'1999-01-01','1999-12-31','SA_MAN',80);
INSERT INTO job_history VALUES(200,'1994-07-01','1998-12-31','AC_ACCOUNT',90);
CREATE TABLE prod_mast(
prod_id integer PRIMARY KEY,
prod_name text(20),
prod_rate integer,
prod_qc text(20) DEFAULT 'OK');
INSERT INTO prod_mast VALUES(1,'Pancakes',75,'OK');
INSERT INTO prod_mast VALUES(2,'Gulha',55,'OK');
INSERT INTO prod_mast VALUES(3,'Pakora',48,'OK');
INSERT INTO prod_mast VALUES(4,'Pizza',200,'OK');
INSERT INTO prod_mast VALUES(5,'Fudge',100,'OK');
INSERT INTO prod_mast VALUES(6,'Candy',95,'OK');
INSERT INTO prod_mast VALUES(7,'Chocolate',150,'OK');
CREATE TABLE prod_backup(
prod_id integer PRIMARY KEY,
prod_name text(20),
prod_rate integer,
prod_qc text(10) DEFAULT 'OK');
INSERT INTO prod_backup VALUES(1,'Pancakes',75,'OK');
INSERT INTO prod_backup VALUES(2,'Gulha',55,'Problems');
INSERT INTO prod_backup VALUES(3,'Pakora',48,'OK');
INSERT INTO prod_backup VALUES(4,'Pizza',200,'OK');
INSERT INTO prod_backup VALUES(5,'Fudge',100,'OK');
INSERT INTO prod_backup VALUES(6,'Candy',95,'Not OK');
INSERT INTO prod_backup VALUES(7,'Chocolate',150,'OK');
CREATE TABLE orders(
ord_no integer PRIMARY KEY,
item_id integer ,
item_name text(20),
ord_qty integer,
cost integer);
INSERT INTO orders VALUES(1,5,'Fudge',100,10000);
INSERT INTO orders VALUES(2,2,'Gulha',95,5225);
INSERT INTO orders VALUES(3,1,'Pancakes',150,11250);
INSERT INTO orders VALUES(4,2,'Gulha',250,13750);
INSERT INTO orders VALUES(5,2,'Gulha',300,16500);
INSERT INTO orders VALUES(6,10,NULL,100,NULL);
INSERT INTO orders VALUES(7,8,NULL,95,NULL);
CREATE TABLE tb1 (c1 INT, c2 CHAR(5), c3 FLOAT);
INSERT INTO tb1 VALUES(1,'1',1.0);
INSERT INTO tb1 VALUES(2,'2',2.0);
INSERT INTO tb1 VALUES(3,'3',3.0);
CREATE TABLE ESERCICIO1(C TEXT, D TEXT);
CREATE TABLE users(name varchar(128), email varchar(128));
CREATE TABLE tags (
    title TEXT,
    description TEXT,
    created TEXT
);
CREATE TABLE s( A int, D int, E int);
CREATE TABLE r (A int, B int);
CREATE TABLE Emor(
ID INT PRIMARY KEY NOT NULL,
NAME TEXT);
CREATE TABLE MIN_SALARY(job_id TEXT,MIN_SALARY);
INSERT INTO MIN_SALARY VALUES('AD_PRES',24000);
INSERT INTO MIN_SALARY VALUES('AD_VP',17000);
INSERT INTO MIN_SALARY VALUES('FI_ACCOUNT',6900);
INSERT INTO MIN_SALARY VALUES('IT_PROG',4200);
INSERT INTO MIN_SALARY VALUES('PU_CLERK',2500);
INSERT INTO MIN_SALARY VALUES('SA_REP',7000);
INSERT INTO MIN_SALARY VALUES('ST_CLERK',2100);
INSERT INTO MIN_SALARY VALUES('ST_MAN',5800);
CREATE TABLE employee_data (employee_name TEXT, item TEXT, rate REAL, quantity INTEGER, date TEXT, id INTEGER PRIMARY KEY);
CREATE TABLE STUDENT(  
   ID INT PRIMARY KEY     NOT NULL,  
   NAME           TEXT    NOT NULL,  
   AGE            INT     NOT NULL,  
   ADDRESS        CHAR(50),  
   FEES         REAL  
);
CREATE TABLE EMPLOYEE_INCOME 
(EMPID NUMBER(10), 
NAME VARCHAR2(20), 
SALARY NUMBER(10));
CREATE TABLE details
(id      number(8,0),
name     varchar2(50),
weight   number(8,0),
turn     number(8,0)
);
CREATE VIEW view_min_sal as
SELECT job_id, min(salary) as 'min_sal'
FROM employees
GROUP BY job_id;
CREATE VIEW COMPANY_VIEW AS
SELECT job_id, min(salary) as 'min_sal'
FROM employees
GROUP BY job_id;
CREATE TRIGGER region_check AFTER INSERT   
ON regions  
BEGIN  
update regions set region_name='MONE' where region_id=999;
update regions set region_name='MONE_999' where region_id=999;






END;
COMMIT;
