-- `642`.alembic_version definition

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
);


-- `642`.items definition

CREATE TABLE `items` (
  `id` int NOT NULL AUTO_INCREMENT,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
);


-- `642`.persons definition

CREATE TABLE `persons` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(200) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
);


-- `642`.customers definition

CREATE TABLE `customers` (
  `cust_id` int NOT NULL,
  `cust_address` varchar(200) NOT NULL,
  `cust_balance` float NOT NULL,
  `max_owing` float NOT NULL,
  PRIMARY KEY (`cust_id`),
  CONSTRAINT `customers_ibfk_1` FOREIGN KEY (`cust_id`) REFERENCES `persons` (`id`)
);


-- `642`.orders definition

CREATE TABLE `orders` (
  `id` int NOT NULL AUTO_INCREMENT,
  `order_customer_id` int NOT NULL,
  `order_date` date NOT NULL,
  `order_number` varchar(100) NOT NULL,
  `order_status` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `order_number` (`order_number`),
  KEY `order_customer_id` (`order_customer_id`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`order_customer_id`) REFERENCES `customers` (`cust_id`)
);


-- `642`.payments definition

CREATE TABLE `payments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `payment_customer_id` int NOT NULL,
  `payment_date` date NOT NULL,
  `payment_amount` float NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `payment_customer_id` (`payment_customer_id`),
  CONSTRAINT `payments_ibfk_1` FOREIGN KEY (`payment_customer_id`) REFERENCES `customers` (`cust_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- `642`.premade_boxes definition

CREATE TABLE `premade_boxes` (
  `id` int NOT NULL,
  `box_size` enum('L','S') NOT NULL,
  `prize` float NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `premade_boxes_ibfk_1` FOREIGN KEY (`id`) REFERENCES `items` (`id`)
);


-- `642`.staff definition

CREATE TABLE `staff` (
  `staff_id` int NOT NULL,
  `date_joined` date NOT NULL,
  `dept_name` varchar(100) NOT NULL,
  PRIMARY KEY (`staff_id`),
  CONSTRAINT `staff_ibfk_1` FOREIGN KEY (`staff_id`) REFERENCES `persons` (`id`)
);


-- `642`.veggies definition

CREATE TABLE `veggies` (
  `veggie_id` int NOT NULL,
  `veg_name` varchar(100) NOT NULL,
  `subtype` varchar(100) NOT NULL,
  `price_per_unit` float NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`veggie_id`),
  CONSTRAINT `veggies_ibfk_1` FOREIGN KEY (`veggie_id`) REFERENCES `items` (`id`)
);


-- `642`.corporate_customers definition

CREATE TABLE `corporate_customers` (
  `corp_id` int NOT NULL,
  `discount_rate` float NOT NULL,
  `max_credit` float NOT NULL,
  `min_balance` float NOT NULL,
  PRIMARY KEY (`corp_id`),
  CONSTRAINT `corporate_customers_ibfk_1` FOREIGN KEY (`corp_id`) REFERENCES `customers` (`cust_id`)
);


-- `642`.credit_card_payments definition

CREATE TABLE `credit_card_payments` (
  `id` int NOT NULL,
  `card_number` varchar(50) NOT NULL,
  `card_expiry_date` date NOT NULL,
  `card_type` enum('VISA','MASTERCARD','AMEX') NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `credit_card_payments_ibfk_1` FOREIGN KEY (`id`) REFERENCES `payments` (`id`)
);


-- `642`.debit_card_payments definition

CREATE TABLE `debit_card_payments` (
  `id` int NOT NULL,
  `bank_name` varchar(100) NOT NULL,
  `debit_card_number` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `debit_card_payments_ibfk_1` FOREIGN KEY (`id`) REFERENCES `payments` (`id`)
);


-- `642`.order_lines definition

CREATE TABLE `order_lines` (
  `id` int NOT NULL AUTO_INCREMENT,
  `order_id` int NOT NULL,
  `item_number` int NOT NULL,
  `amount` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `order_id` (`order_id`),
  KEY `item_number` (`item_number`),
  CONSTRAINT `order_lines_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`),
  CONSTRAINT `order_lines_ibfk_2` FOREIGN KEY (`item_number`) REFERENCES `items` (`id`)
);