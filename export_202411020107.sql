INSERT INTO `642`.corporate_customers (corp_id,discount_rate,max_credit,min_balance) VALUES
	 (3,54.0,45880.0,282.0),
	 (6,24.0,68838.0,400.0),
	 (9,40.0,91771.0,452.0),
	 (12,59.0,61362.0,618.0),
	 (15,10.0,25004.0,222.0),
	 (18,5.0,47294.0,856.0),
	 (21,10.0,30403.0,788.0),
	 (24,7.0,92394.0,404.0),
	 (27,87.0,34420.0,950.0),
	 (30,95.0,61108.0,178.0);
INSERT INTO `642`.credit_card_payments (id,card_number,card_expiry_date,card_type) VALUES
	 (3,'4381994208335164098','2031-08-01','MASTERCARD'),
	 (4,'4329806946203837736','2027-01-01','MASTERCARD'),
	 (6,'6011197292316674','2027-06-01','AMEX');
INSERT INTO `642`.customers (cust_id,cust_address,cust_balance,max_owing) VALUES
	 (1,'3811 Morrison Centers Apt. 778
Wardchester, TX 58114',4745.0,8583.0),
	 (3,'88716 Vanessa Parks Apt. 104
East Veronicaport, GA 10903',3206.0,5089.0),
	 (4,'5925 Timothy Lodge
New Levi, MD 40030',8336.0,2247.0),
	 (6,'5974 Jeffrey Crossroad Suite 684
West Tinaland, GA 69202',7160.0,7060.0),
	 (7,'32168 Michelle Vista Apt. 642
Teresatown, AS 85369',2171.0,1809.0),
	 (9,'52158 Matthew Curve
Loganport, VI 72259',1272.0,5140.0),
	 (10,'9647 Susan Pine
West Kristenberg, SD 45292',7886.0,8888.0),
	 (12,'25604 Shannon Terrace
Lake Dustinberg, CO 96686',6690.0,7321.0),
	 (13,'47560 Acosta Prairie Suite 387
South Michaelview, WI 78890',5201.0,9961.0),
	 (15,'44071 Andres Manors
South Trevor, NH 11002',690.0,1750.0);
INSERT INTO `642`.customers (cust_id,cust_address,cust_balance,max_owing) VALUES
	 (16,'07195 Joseph Lodge
New Teresa, NC 45603',4250.0,606.0),
	 (18,'Unit 5796 Box 7220
DPO AA 02526',9234.0,2791.0),
	 (19,'5304 Ramos View Apt. 790
Sandraport, TN 41881',9429.0,7049.0),
	 (21,'1592 Kyle Centers Suite 659
Walkerberg, NM 99722',9290.0,5365.0),
	 (22,'989 Jeffrey Rapid Apt. 476
New Benjamin, MP 35503',6873.0,7513.0),
	 (24,'PSC 3275, Box 7884
APO AP 31100',2736.0,4998.0),
	 (25,'Unit 9716 Box 1520
DPO AE 69401',7726.0,9335.0),
	 (27,'PSC 8740, Box 4200
APO AE 67767',8676.0,2516.0),
	 (28,'55858 Caroline Ville
Mcdonaldmouth, PA 90506',2095.0,669.0),
	 (30,'903 Peter Parkways
Christinafurt, MI 68136',4204.0,6525.0);
INSERT INTO `642`.debit_card_payments (id,bank_name,debit_card_number) VALUES
	 (1,'Moss-Callahan','GFFY23030133318248'),
	 (2,'Roberson-Contreras','EFNB65064565656750'),
	 (5,'Long-Ford','EZOD83437413638093'),
	 (7,'Johnson-Villegas','TPKT87841317118136'),
	 (8,'Watson-Davis','ILAA82343131178426'),
	 (9,'Hernandez-Glover','MUMJ88530036995543'),
	 (10,'Cochran-Wilkins','CUUU62394784076122');
INSERT INTO `642`.items (`type`) VALUES
	 ('VEGGIE'),
	 ('VEGGIE'),
	 ('VEGGIE'),
	 ('VEGGIE'),
	 ('VEGGIE'),
	 ('PREMADE_BOX'),
	 ('PREMADE_BOX'),
	 ('VEGGIE'),
	 ('VEGGIE'),
	 ('VEGGIE');
INSERT INTO `642`.items (`type`) VALUES
	 ('VEGGIE'),
	 ('VEGGIE'),
	 ('PREMADE_BOX'),
	 ('PREMADE_BOX');
INSERT INTO `642`.order_lines (order_id,item_number,amount) VALUES
	 (1,1,6),
	 (2,2,1),
	 (3,3,2),
	 (4,4,9),
	 (5,5,7),
	 (6,8,9),
	 (7,9,10),
	 (8,10,5),
	 (9,11,4),
	 (10,12,9);
INSERT INTO `642`.orders (order_customer_id,order_date,order_number,order_status) VALUES
	 (1,'2024-08-05','ORD-31086','Shipped'),
	 (4,'2024-10-27','ORD-48020','Completed'),
	 (7,'2024-01-06','ORD-39790','Completed'),
	 (10,'2024-04-16','ORD-25151','Pending'),
	 (13,'2024-02-16','ORD-71357','Completed'),
	 (16,'2024-09-20','ORD-91912','Pending'),
	 (19,'2024-05-15','ORD-27781','Completed'),
	 (22,'2024-08-23','ORD-83832','Completed'),
	 (25,'2024-06-15','ORD-34032','Shipped'),
	 (28,'2024-06-13','ORD-75528','Completed');
INSERT INTO `642`.payments (payment_customer_id,payment_date,payment_amount,`type`) VALUES
	 (1,'2024-08-27',1186.0,'DEBIT_CARD'),
	 (4,'2024-08-12',9616.0,'DEBIT_CARD'),
	 (7,'2024-05-11',5770.0,'CREDIT_CARD'),
	 (10,'2024-09-03',60.0,'CREDIT_CARD'),
	 (13,'2024-10-24',9407.0,'DEBIT_CARD'),
	 (16,'2024-09-16',37.0,'CREDIT_CARD'),
	 (19,'2024-02-26',3323.0,'DEBIT_CARD'),
	 (22,'2024-07-15',70.0,'DEBIT_CARD'),
	 (25,'2024-05-25',3823.0,'DEBIT_CARD'),
	 (28,'2024-09-19',6507.0,'DEBIT_CARD');
INSERT INTO `642`.persons (first_name,last_name,username,password,`type`) VALUES
	 ('Kimberly','Scott','sbradley','password','CUSTOMER'),
	 ('Stephen','Burke','roger55','password','STAFF'),
	 ('Kendra','Chapman','christine87','password','CUSTOMER'),
	 ('Brittany','Walters','omar08','password','CUSTOMER'),
	 ('Jessica','Baker','christopher84','password','STAFF'),
	 ('Cassandra','Allen','njohnson','password','CUSTOMER'),
	 ('Brandi','Anderson','phillipsrichard','password','CUSTOMER'),
	 ('Elizabeth','Lee','jerrycole','password','STAFF'),
	 ('Hunter','Carroll','deniseramirez','password','CUSTOMER'),
	 ('Jennifer','Hunt','benjamin14','password','CUSTOMER');
INSERT INTO `642`.persons (first_name,last_name,username,password,`type`) VALUES
	 ('Sheila','Martinez','ijenkins','password','STAFF'),
	 ('Brittany','Wells','david59','password','CUSTOMER'),
	 ('Nicole','Rivera','mneal','password','CUSTOMER'),
	 ('Mary','Davis','erikaramirez','password','STAFF'),
	 ('David','Lewis','kellyterry','password','CUSTOMER'),
	 ('Nicole','Jacobson','sara14','password','CUSTOMER'),
	 ('Brent','Graham','qholt','password','STAFF'),
	 ('Michele','Christian','loripatterson','password','CUSTOMER'),
	 ('Frederick','Hunt','john80','password','CUSTOMER'),
	 ('Louis','Woods','whitedenise','password','STAFF');
INSERT INTO `642`.persons (first_name,last_name,username,password,`type`) VALUES
	 ('Dennis','Nguyen','morganchoi','password','CUSTOMER'),
	 ('David','Evans','brettsandoval','password','CUSTOMER'),
	 ('Laura','Alvarado','andreawilson','password','STAFF'),
	 ('Brady','Lozano','williamhenderson','password','CUSTOMER'),
	 ('Julie','Lara','davidmarshall','password','CUSTOMER'),
	 ('James','Holmes','ethomas','password','STAFF'),
	 ('Mark','Robbins','ihughes','password','CUSTOMER'),
	 ('Monica','Jensen','gallagherwhitney','password','CUSTOMER'),
	 ('Sonya','Wong','greenjamie','password','STAFF'),
	 ('Christina','Ward','kennethperry','password','CUSTOMER');
INSERT INTO `642`.premade_boxes (id,box_size,prize,quantity) VALUES
	 (6,'L',770.0,100),
	 (7,'S',320.0,100),
	 (13,'L',476.0,100),
	 (14,'S',561.0,100);
INSERT INTO `642`.staff (staff_id,date_joined,dept_name) VALUES
	 (2,'2022-07-03','Inc'),
	 (5,'2022-08-08','Group'),
	 (8,'2021-04-01','Group'),
	 (11,'2022-12-14','PLC'),
	 (14,'2022-08-21','Ltd'),
	 (17,'2024-09-04','and Sons'),
	 (20,'2023-06-09','LLC'),
	 (23,'2020-10-01','and Sons'),
	 (26,'2022-04-19','LLC'),
	 (29,'2021-05-11','Inc');
INSERT INTO `642`.veggies (veggie_id,veg_name,subtype,price_per_unit,quantity) VALUES
	 (1,'according','PACK_VEGGIE',187.0,100),
	 (2,'card','WEIGHTED_VEGGIE',98.0,100),
	 (3,'two','UNIT_PRICE_VEGGIE',36.0,100),
	 (4,'region','PACK_VEGGIE',142.0,100),
	 (5,'dream','WEIGHTED_VEGGIE',30.0,100),
	 (8,'at','UNIT_PRICE_VEGGIE',34.0,100),
	 (9,'look','PACK_VEGGIE',509.0,100),
	 (10,'lay','WEIGHTED_VEGGIE',86.0,100),
	 (11,'sound','WEIGHTED_VEGGIE',36.0,100),
	 (12,'nearly','WEIGHTED_VEGGIE',38.0,100);
