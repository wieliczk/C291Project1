
@a2_setup_new

INSERT INTO people VALUES
	('127222567', 'Joe A', 133.67, 100.00, 'Green', 'Black', '123 Edmonton AB', 'm', DATE '1990-05-06');
INSERT INTO people VALUES
	('127222568', 'Joe B', 133.67, 100.00, 'Blue', 'Black', '123 Edmonton AB', 'm', DATE '1990-05-06');
INSERT INTO people VALUES
	('127222569', 'Joe C', 133.67, 100.00, 'Green', 'Black', '123 Calgary AB', 'm', DATE '1990-05-06');
INSERT INTO people VALUES
	('127222561', 'No Licence Dude', 133.67, 100.00, 'Black', 'Brown', '123 Edmonton AB', 'm', DATE '1990-05-06');
INSERT INTO people VALUES
	('127222562', 'Joe E', 133.67, 100.00, 'Black', 'Red', '123 Calgary AB', 'm', DATE '1990-05-06');
INSERT INTO people VALUES
	('127222563', 'Joe F', 133.67, 100.00, 'Brown', 'Black', '123 Edmonton AB', 'm', DATE '1990-05-06');
INSERT INTO people VALUES
	('127222560', 'SUV Owner', 133.67, 100.00, 'Brown', 'Black', '123 Ft Macmaurry AB', 'm', DATE '1980-05-06');


INSERT INTO drive_licence VALUES
	(1, '127222567', 'basic', NULL, DATE '2000-01-01', DATE '2015-01-01');
INSERT INTO drive_licence VALUES
	(2, '127222568', 'basic', NULL, DATE '2000-01-01', DATE '2015-01-01');
INSERT INTO drive_licence VALUES
	(3, '127222569', 'advanced', NULL, DATE '2000-01-01', DATE '2015-01-01');
INSERT INTO drive_licence VALUES
	(4, '127222562', 'basic', NULL, DATE '2000-01-01', DATE '2015-01-01');
INSERT INTO drive_licence VALUES
	(5, '127222563', 'nondriving', NULL, DATE '2000-01-01', DATE '2015-01-01');
INSERT INTO drive_licence VALUES
	(6, '127222560', 'basic', NULL, DATE '2000-01-01', DATE '2015-01-01');


INSERT INTO vehicle_type VALUES
	(1, 'Car');
INSERT INTO vehicle_type VALUES
	(2, 'SUV');
INSERT INTO vehicle_type VALUES
	(3, 'Van');


INSERT INTO vehicle VALUES
	('1A', 'Ford', 'Impala', 2006, 'Blue', 2);
INSERT INTO vehicle VALUES
	('2A', 'Ford', 'Focus', 2010, 'Red', 2);
INSERT INTO vehicle VALUES
	('3A', 'Nissan', 'Ultima', 2011, 'White', 1);
INSERT INTO vehicle VALUES
	('4A', 'Nissan', 'BigVan', 2012, 'Black', 3);
INSERT INTO vehicle VALUES
	('5B', 'Tesla', 'Volt', 2013, 'Red', 1);
INSERT INTO vehicle VALUES
	('6B', 'Tesla', 'MarkX', 2011, 'White', 1);
INSERT INTO vehicle VALUES
	('6C', 'Tesla', 'MarkX', 2011, 'White', 1);
INSERT INTO vehicle VALUES
	('1D', 'Nissan', 'BigTruck', 2012, 'Black', 2);
INSERT INTO vehicle VALUES
	('2D', 'Nissan', 'BigTruck', 2012, 'White', 2);
INSERT INTO vehicle VALUES
	('3D', 'Nissan', 'BigTruck', 2012, 'Green', 2);


INSERT INTO auto_sale VALUES
	(1, '127222567', '127222568', '1A', DATE '2011-01-01', 10000.00);
INSERT INTO auto_sale VALUES
	(2, '127222567', '127222568', '2A', DATE '2010-01-01', 12000.00);
INSERT INTO auto_sale VALUES
	(3, '127222567', '127222568', '3A', DATE '2010-01-01', 20000.00);
INSERT INTO auto_sale VALUES
	(4, '127222567', '127222568', '4A', DATE '2011-01-01', 10000.00);
INSERT INTO auto_sale VALUES
	(5, '127222567', '127222568', '5B', DATE '2012-01-01', 11000.00);
INSERT INTO auto_sale VALUES
	(6, '127222567', '127222568', '6B', DATE '2013-01-01', 20000.00);
INSERT INTO auto_sale VALUES
	(7, '127222567', '127222568', '1D', DATE '2014-01-01', 32000.00);
INSERT INTO auto_sale VALUES
	(8, '127222567', '127222568', '2D', DATE '2010-01-01', 8000.00);
INSERT INTO auto_sale VALUES
	(9, '127222567', '127222568', '3D', DATE '2011-01-01', 30000.00);


INSERT INTO ticket_type VALUES
	('parking', 30.00);
INSERT INTO ticket_type VALUES
	('speeding', 50.00);
INSERT INTO ticket_type VALUES
	('lights', 20.00);


INSERT INTO ticket VALUES
	(1, '127222567', '1A', '127222561', 'speeding', DATE '2015-08-01', 'Edmonton', 'BlahBlah');
INSERT INTO ticket VALUES
	(2, '127222568', '2A', '127222561', 'lights', DATE '2015-04-01', 'Edmonton', 'BlahBlah');
INSERT INTO ticket VALUES
	(3, '127222568', '2A', '127222561', 'lights', DATE '2015-04-01', 'Edmonton', 'BlahBlah');
INSERT INTO ticket VALUES
	(4, '127222568', '2A', '127222561', 'speeding', DATE '2015-04-01', 'Edmonton', 'BlahBlah');
INSERT INTO ticket VALUES
	(5, '127222569', '2A', '127222561', 'parking', DATE '2014-06-01', 'Edmonton', 'BlahBlah');
INSERT INTO ticket VALUES
	(6, '127222562', '5B', '127222561', 'speeding', DATE '2015-07-01', 'Edmonton', 'BlahBlah');
INSERT INTO ticket VALUES
	(7, '127222563', '6B', '127222561', 'speeding', DATE '2014-07-01', 'Edmonton', 'BlahBlah');
INSERT INTO ticket VALUES
	(8, '127222560', '1D', '127222561', 'parking', DATE '2015-07-01', 'Edmonton', 'BlahBlah');
INSERT INTO ticket VALUES
	(9, '127222560', '1D', '127222561', 'parking', DATE '2015-07-01', 'Edmonton', 'BlahBlah');
INSERT INTO ticket VALUES
	(10, '127222567', '1A', '127222561', 'speeding', DATE '2011-08-01', 'Edmonton', 'BlahBlah');
INSERT INTO ticket VALUES
	(11, '127222567', '1A', '127222561', 'speeding', DATE '2013-08-01', 'Edmonton', 'BlahBlah');
INSERT INTO ticket VALUES
	(12, '127222567', '1A', '127222561', 'speeding', DATE '2011-08-01', 'Edmonton', 'BlahBlah');


INSERT INTO owner VALUES
	('127222567', '1A', 'y');
INSERT INTO owner VALUES
	('127222568', '2A', 'y');
INSERT INTO owner VALUES
	('127222569', '2A', 'n');
INSERT INTO owner VALUES
	('127222561', '4A', 'y');
INSERT INTO owner VALUES
	('127222562', '5B', 'y');
INSERT INTO owner VALUES
	('127222563', '6B', 'y');
INSERT INTO owner VALUES
	('127222560', '1D', 'y');
INSERT INTO owner VALUES
	('127222560', '2D', 'y');
INSERT INTO owner VALUES
	('127222560', '3D', 'y');


