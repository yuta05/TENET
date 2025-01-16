BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "customers" (
	"customer_id"	TEXT,
	"first_name"	TEXT,
	"last_name"	TEXT,
	"email"	TEXT,
	"phone"	TEXT,
	"ip_address"	TEXT,
	"address_line"	TEXT,
	"street_address"	TEXT,
	"city_address"	TEXT,
	"state_address"	TEXT,
	"zip_code"	INTEGER,
	"country"	TEXT,
	"account_status"	TEXT,
	"preferred_contact_method"	TEXT,
	"preferred_language"	TEXT
);
CREATE TABLE IF NOT EXISTS "installation_requirements" (
	"product_id"	TEXT,
	"requirement_type"	TEXT,
	"requirement_key"	TEXT,
	"requirement_value"	TEXT
);
CREATE TABLE IF NOT EXISTS "installation_slots" (
	"slot_id"	INTEGER,
	"date"	TEXT,
	"time"	TEXT,
	"duration"	TEXT,
	"available"	TEXT
);
CREATE TABLE IF NOT EXISTS "orders" (
	"order_id"	TEXT,
	"customer_id"	TEXT,
	"product_id"	TEXT,
	"order_date"	TEXT,
	"status"	TEXT,
	"delivery_status"	TEXT,
	"estimated_delivery"	TEXT
);
CREATE TABLE IF NOT EXISTS "product_compatibility" (
	"product_id"	TEXT,
	"compatible_with"	TEXT
);
CREATE TABLE IF NOT EXISTS "product_recommendations" (
	"product_id"	TEXT,
	"location_type"	TEXT,
	"recommendation_level"	TEXT,
	"recommendation_reason"	TEXT
);
CREATE TABLE IF NOT EXISTS "product_specifications" (
	"product_id"	TEXT,
	"spec_key"	TEXT,
	"spec_value"	TEXT
);
CREATE TABLE IF NOT EXISTS "products" (
	"product_id"	TEXT,
	"model"	TEXT,
	"type"	TEXT,
	"name"	TEXT,
	"description"	TEXT,
	"stock_status"	TEXT,
	"price"	INTEGER,
	"installation_type"	TEXT
);
CREATE TABLE IF NOT EXISTS "region_requirements" (
	"country"	TEXT,
	"state"	TEXT,
	"city"	TEXT,
	"permit_required"	TEXT,
	"electrical_inspection"	TEXT,
	"zoning_restrictions"	TEXT
);
CREATE TABLE IF NOT EXISTS "required_tools" (
	"template_id"	INTEGER,
	"tool_name"	TEXT
);
CREATE TABLE IF NOT EXISTS "work_order_steps" (
	"template_id"	INTEGER,
	"step_number"	INTEGER,
	"description"	TEXT,
	"estimated_time"	TEXT
);
CREATE TABLE IF NOT EXISTS "work_order_templates" (
	"template_id"	INTEGER,
	"product_id"	TEXT,
	"template_type"	TEXT
);
INSERT INTO "customers" VALUES ('CUST-001','Mark','Watts','mark.watts@email.com','1-555-123','181.128.215.235',NULL,'123 Main Street','Springfield','IL',62701,'USA','active','email','en');
INSERT INTO "installation_requirements" VALUES ('F100-WALL','electrical','voltage','240V');
INSERT INTO "installation_requirements" VALUES ('F100-WALL','electrical','circuit','dedicated');
INSERT INTO "installation_requirements" VALUES ('F100-WALL','electrical','amperage','48A');
INSERT INTO "installation_requirements" VALUES ('F100-WALL','electrical','wire_gauge','6 AWG');
INSERT INTO "installation_requirements" VALUES ('F100-WALL','electrical','grounding','required');
INSERT INTO "installation_requirements" VALUES ('F100-WALL','mounting','wall_type','concrete|brick|wood-fram');
INSERT INTO "installation_requirements" VALUES ('F100-WALL','mounting','minimum_height','1.2m');
INSERT INTO "installation_requirements" VALUES ('F100-WALL','mounting','maximum_height','1.5m');
INSERT INTO "installation_requirements" VALUES ('F100-WALL','mounting','clearance_sides','30cm');
INSERT INTO "installation_requirements" VALUES ('F100-WALL','mounting','clearance_front','1m');
INSERT INTO "installation_requirements" VALUES ('F100-WALL','environmental','indoor_rated','TRUE');
INSERT INTO "installation_requirements" VALUES ('F100-WALL','environmental','outdoor_rated','TRUE');
INSERT INTO "installation_requirements" VALUES ('F100-WALL','environmental','min_temperature','-30');
INSERT INTO "installation_requirements" VALUES ('F100-WALL','environmental','max_temperature','50');
INSERT INTO "installation_requirements" VALUES ('F100-WALL','environmental','ip_rating','IP65');
INSERT INTO "installation_slots" VALUES (1,'2024-07-21','9:00','4-6 hours','TRUE');
INSERT INTO "installation_slots" VALUES (2,'2024-07-22','13:00','4-6 hours','TRUE');
INSERT INTO "installation_slots" VALUES (3,'2024-07-27','9:00','4-6 hours','TRUE');
INSERT INTO "installation_slots" VALUES (4,'2024-07-28','13:00','4-6 hours','TRUE');
INSERT INTO "orders" VALUES ('ORD-2024-0715-001','CUST-001','PX-VPX1B','2024-07-15','confirmed','scheduled','2024-Q3');
INSERT INTO "product_compatibility" VALUES ('P50-HOME','PX-VPX1B');
INSERT INTO "product_compatibility" VALUES ('F100-WALL','PX-VPX1B');
INSERT INTO "product_compatibility" VALUES ('U150-PORT','PX-VPX1B');
INSERT INTO "product_compatibility" VALUES ('S200-COMM','PX-VPX1B');
INSERT INTO "product_recommendations" VALUES ('F100-WALL','garage','high','Optimized for garage installation');
INSERT INTO "product_recommendations" VALUES ('F100-WALL','garage','high','Fast charging capability');
INSERT INTO "product_recommendations" VALUES ('F100-WALL','garage','high','Latest charging standards support');
INSERT INTO "product_recommendations" VALUES ('F100-WALL','garage','high','Hardwired connection option');
INSERT INTO "product_specifications" VALUES ('PX-VPX1B','battery_capacity','85kWh');
INSERT INTO "product_specifications" VALUES ('PX-VPX1B','range','300 miles');
INSERT INTO "product_specifications" VALUES ('PX-VPX1B','charging_standards','CCS|Type 2');
INSERT INTO "product_specifications" VALUES ('P50-HOME','power','7.4kW');
INSERT INTO "product_specifications" VALUES ('P50-HOME','voltage','240V');
INSERT INTO "product_specifications" VALUES ('P50-HOME','current','32A');
INSERT INTO "product_specifications" VALUES ('P50-HOME','connection_type','Type 2');
INSERT INTO "product_specifications" VALUES ('F100-WALL','power','11kW');
INSERT INTO "product_specifications" VALUES ('F100-WALL','voltage','240V');
INSERT INTO "product_specifications" VALUES ('F100-WALL','current','48A');
INSERT INTO "product_specifications" VALUES ('F100-WALL','connection_type','Type 2');
INSERT INTO "product_specifications" VALUES ('U150-PORT','power','9.6kW');
INSERT INTO "product_specifications" VALUES ('U150-PORT','voltage','240V');
INSERT INTO "product_specifications" VALUES ('U150-PORT','current','40A');
INSERT INTO "product_specifications" VALUES ('U150-PORT','connection_type','Type 2');
INSERT INTO "product_specifications" VALUES ('S200-COMM','power','22kW');
INSERT INTO "product_specifications" VALUES ('S200-COMM','voltage','400V');
INSERT INTO "product_specifications" VALUES ('S200-COMM','current','32A');
INSERT INTO "product_specifications" VALUES ('S200-COMM','connection_type','Type 2');
INSERT INTO "products" VALUES ('PX-VPX1B','PalX-VPX1B','vehicle','PalX Electric Vehicle','Premium Electric Vehicle Model VPX1B','in_stock',45000,'n/a');
INSERT INTO "products" VALUES ('P50-HOME','P50-Home','home_charger','P50-Home Charger','Basic home charging solution','out_stock',699,'wall-mounted');
INSERT INTO "products" VALUES ('F100-WALL','F100-Wall','home_charger','F100-Wall Charger','Premium wall-mounted charging','in_stock',999,'wall-mounted');
INSERT INTO "products" VALUES ('U150-PORT','U150-Port','home_charger','U150-Portable Charger','Flexible portable charging solution','in_stock',799,'portable');
INSERT INTO "products" VALUES ('S200-COMM','S200-Comm','commercial','S200-Commercial Charger','Heavy-duty commercial charging station','in_stock',2499,'floor-mounted');
INSERT INTO "region_requirements" VALUES ('USA','IL','Springfield','FALSE','TRUE','FALSE');
INSERT INTO "required_tools" VALUES (1,'Circuit tester');
INSERT INTO "required_tools" VALUES (1,'Wire stripper');
INSERT INTO "required_tools" VALUES (1,'Conduit bende');
INSERT INTO "required_tools" VALUES (1,'Power drill');
INSERT INTO "required_tools" VALUES (1,'Level');
INSERT INTO "required_tools" VALUES (1,'Socket set');
INSERT INTO "required_tools" VALUES (1,'Insulated glove');
INSERT INTO "required_tools" VALUES (1,'Safety glasses');
INSERT INTO "required_tools" VALUES (1,'Work boots');
INSERT INTO "required_tools" VALUES (1,'Hard hat');
INSERT INTO "work_order_steps" VALUES (1,1,'Site inspection and preparation','30min');
INSERT INTO "work_order_steps" VALUES (1,2,'Circuit assessment and testing','30min');
INSERT INTO "work_order_steps" VALUES (1,3,'New circuit installation if needed','120min');
INSERT INTO "work_order_steps" VALUES (1,4,'Charger mounting and installation','60min');
INSERT INTO "work_order_steps" VALUES (1,5,'System testing and verification','30min');
INSERT INTO "work_order_steps" VALUES (1,6,'Customer orientation','30min');
INSERT INTO "work_order_templates" VALUES (1,'F100-WALL','installation');
COMMIT;
