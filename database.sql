-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: bank_app_db
-- ------------------------------------------------------
-- Server version	8.0.44

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts`
--

DROP TABLE IF EXISTS `accounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts` (
  `account_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `branch_id` int DEFAULT NULL,
  `account_type` enum('SAVINGS','CURRENT') DEFAULT NULL,
  `balance` decimal(12,2) DEFAULT '0.00',
  `acc_status` enum('ACTIVE','FROZEN') DEFAULT 'ACTIVE',
  PRIMARY KEY (`account_id`),
  KEY `fk_users` (`user_id`),
  KEY `fk_branch` (`branch_id`),
  CONSTRAINT `fk_branch` FOREIGN KEY (`branch_id`) REFERENCES `branches` (`branch_id`),
  CONSTRAINT `fk_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts`
--

LOCK TABLES `accounts` WRITE;
/*!40000 ALTER TABLE `accounts` DISABLE KEYS */;
INSERT INTO `accounts` VALUES (1,11,1,'SAVINGS',26000.00,'ACTIVE'),(2,11,1,'CURRENT',13500.00,'ACTIVE'),(3,12,2,'SAVINGS',61500.00,'ACTIVE'),(4,13,1,'SAVINGS',15500.00,'ACTIVE'),(5,14,3,'CURRENT',94200.00,'ACTIVE'),(6,15,4,'SAVINGS',11300.00,'ACTIVE'),(7,16,2,'CURRENT',39000.00,'ACTIVE'),(8,17,3,'SAVINGS',33000.00,'ACTIVE'),(9,18,1,'CURRENT',62500.00,'ACTIVE'),(10,19,4,'SAVINGS',52000.00,'ACTIVE'),(11,20,2,'SAVINGS',18000.00,'ACTIVE');
/*!40000 ALTER TABLE `accounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `branches`
--

DROP TABLE IF EXISTS `branches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `branches` (
  `branch_id` int NOT NULL AUTO_INCREMENT,
  `branch_name` varchar(100) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `branch_status` enum('ACTIVE','INACTIVE') DEFAULT 'ACTIVE',
  PRIMARY KEY (`branch_id`),
  UNIQUE KEY `branch_name` (`branch_name`,`location`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `branches`
--

LOCK TABLES `branches` WRITE;
/*!40000 ALTER TABLE `branches` DISABLE KEYS */;
INSERT INTO `branches` VALUES (1,'Delhi','North Delhi','ACTIVE'),(2,'Mumbai','Andheri','ACTIVE'),(3,'Bangalore','Whitefield','ACTIVE'),(4,'Chandigarh','Sector 17','ACTIVE');
/*!40000 ALTER TABLE `branches` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `customer_account_view`
--

DROP TABLE IF EXISTS `customer_account_view`;
/*!50001 DROP VIEW IF EXISTS `customer_account_view`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `customer_account_view` AS SELECT 
 1 AS `account_id`,
 1 AS `user_id`,
 1 AS `branch_name`,
 1 AS `account_type`,
 1 AS `balance`,
 1 AS `acc_status`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `customer_transactions_view`
--

DROP TABLE IF EXISTS `customer_transactions_view`;
/*!50001 DROP VIEW IF EXISTS `customer_transactions_view`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `customer_transactions_view` AS SELECT 
 1 AS `transaction_id`,
 1 AS `account_id`,
 1 AS `related_account_id`,
 1 AS `transaction_type`,
 1 AS `amount`,
 1 AS `transaction_date_time`,
 1 AS `user_id`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `loans`
--

DROP TABLE IF EXISTS `loans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loans` (
  `loan_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `branch_id` int NOT NULL,
  `loan_type` enum('HOME','PERSONAL','VEHICLE','EDUCATION') NOT NULL,
  `amount` decimal(12,2) NOT NULL,
  `loan_status` enum('PENDING','APPROVED','REJECTED') DEFAULT 'PENDING',
  PRIMARY KEY (`loan_id`),
  KEY `fk_loan_user` (`user_id`),
  KEY `fk_loan_branch` (`branch_id`),
  CONSTRAINT `fk_loan_branch` FOREIGN KEY (`branch_id`) REFERENCES `branches` (`branch_id`),
  CONSTRAINT `fk_loan_user` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loans`
--

LOCK TABLES `loans` WRITE;
/*!40000 ALTER TABLE `loans` DISABLE KEYS */;
INSERT INTO `loans` VALUES (1,11,1,'HOME',500000.00,'APPROVED'),(2,12,2,'PERSONAL',75000.00,'PENDING'),(3,13,1,'VEHICLE',300000.00,'REJECTED'),(4,14,3,'EDUCATION',450000.00,'APPROVED'),(5,15,4,'PERSONAL',120000.00,'PENDING'),(6,16,2,'HOME',1500000.00,'APPROVED'),(7,17,3,'VEHICLE',600000.00,'PENDING'),(8,18,1,'PERSONAL',50000.00,'REJECTED'),(9,19,4,'HOME',900000.00,'APPROVED'),(10,20,2,'EDUCATION',350000.00,'PENDING');
/*!40000 ALTER TABLE `loans` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transactions`
--

DROP TABLE IF EXISTS `transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transactions` (
  `transaction_id` int NOT NULL AUTO_INCREMENT,
  `account_id` int NOT NULL,
  `related_account_id` int DEFAULT NULL,
  `transaction_type` enum('DEPOSIT','WITHDRAW','TRANSFER') DEFAULT NULL,
  `amount` decimal(12,2) NOT NULL,
  `transaction_date_time` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`transaction_id`),
  KEY `fk_transaction_account` (`account_id`),
  KEY `fk_related_account` (`related_account_id`),
  CONSTRAINT `fk_related_account` FOREIGN KEY (`related_account_id`) REFERENCES `accounts` (`account_id`),
  CONSTRAINT `fk_transaction_account` FOREIGN KEY (`account_id`) REFERENCES `accounts` (`account_id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions`
--

LOCK TABLES `transactions` WRITE;
/*!40000 ALTER TABLE `transactions` DISABLE KEYS */;
INSERT INTO `transactions` VALUES (1,1,NULL,'DEPOSIT',5000.00,'2026-07-16 16:52:11'),(2,2,NULL,'DEPOSIT',2500.00,'2026-07-16 16:52:11'),(3,3,NULL,'DEPOSIT',7000.00,'2026-07-16 16:52:11'),(4,4,NULL,'DEPOSIT',10000.00,'2026-07-16 16:52:11'),(5,5,NULL,'DEPOSIT',3500.00,'2026-07-16 16:52:11'),(6,6,NULL,'DEPOSIT',2000.00,'2026-07-16 16:52:11'),(7,7,NULL,'DEPOSIT',8000.00,'2026-07-16 16:52:11'),(8,8,NULL,'DEPOSIT',6000.00,'2026-07-16 16:52:11'),(9,9,NULL,'DEPOSIT',4000.00,'2026-07-16 16:52:11'),(10,10,NULL,'DEPOSIT',12000.00,'2026-07-16 16:52:11'),(11,11,NULL,'DEPOSIT',5000.00,'2026-07-16 16:52:11'),(12,1,NULL,'WITHDRAW',1500.00,'2026-07-16 16:52:20'),(13,2,NULL,'WITHDRAW',500.00,'2026-07-16 16:52:20'),(14,3,NULL,'WITHDRAW',2000.00,'2026-07-16 16:52:20'),(15,4,NULL,'WITHDRAW',12000.00,'2026-07-16 16:52:20'),(16,5,NULL,'WITHDRAW',1000.00,'2026-07-16 16:52:20'),(17,7,NULL,'WITHDRAW',2500.00,'2026-07-16 16:52:20'),(18,8,NULL,'WITHDRAW',5000.00,'2026-07-16 16:52:20'),(19,9,NULL,'WITHDRAW',3000.00,'2026-07-16 16:52:20'),(20,10,NULL,'WITHDRAW',4000.00,'2026-07-16 16:52:20'),(21,1,3,'TRANSFER',2500.00,'2026-07-16 16:52:27'),(22,3,1,'TRANSFER',2500.00,'2026-07-16 16:52:27'),(23,2,5,'TRANSFER',1500.00,'2026-07-16 16:52:27'),(24,5,2,'TRANSFER',1500.00,'2026-07-16 16:52:27'),(25,4,8,'TRANSFER',5000.00,'2026-07-16 16:52:27'),(26,8,4,'TRANSFER',5000.00,'2026-07-16 16:52:27'),(27,6,10,'TRANSFER',3500.00,'2026-07-16 16:52:27'),(28,10,6,'TRANSFER',3500.00,'2026-07-16 16:52:27'),(29,7,9,'TRANSFER',4000.00,'2026-07-16 16:52:27'),(30,9,7,'TRANSFER',4000.00,'2026-07-16 16:52:27'),(31,11,2,'TRANSFER',2000.00,'2026-07-16 16:52:27'),(32,2,11,'TRANSFER',2000.00,'2026-07-16 16:52:27'),(33,3,1,'TRANSFER',1000.00,'2026-07-16 16:52:27'),(34,1,3,'TRANSFER',1000.00,'2026-07-16 16:52:27'),(35,5,6,'TRANSFER',800.00,'2026-07-16 16:52:27'),(36,6,5,'TRANSFER',800.00,'2026-07-16 16:52:27'),(37,10,4,'TRANSFER',4500.00,'2026-07-16 16:52:27'),(38,4,10,'TRANSFER',4500.00,'2026-07-16 16:52:27'),(39,9,7,'TRANSFER',2500.00,'2026-07-16 16:52:27'),(40,7,9,'TRANSFER',2500.00,'2026-07-16 16:52:27'),(41,1,2,'TRANSFER',1000.00,'2026-07-16 17:07:04'),(42,2,1,'TRANSFER',1000.00,'2026-07-16 17:07:04'),(43,2,NULL,'DEPOSIT',1000.00,'2026-07-16 22:37:12'),(44,2,5,'TRANSFER',1000.00,'2026-07-16 22:40:13'),(45,5,2,'TRANSFER',1000.00,'2026-07-16 22:40:13');
/*!40000 ALTER TABLE `transactions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `role` enum('SUPER_ADMIN','BRANCH_HEAD','STAFF','CUSTOMER') DEFAULT NULL,
  `user_status` enum('ACTIVE','INACTIVE') DEFAULT 'ACTIVE',
  `branch_id` int DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_name` (`user_name`),
  KEY `fk_user_branch` (`branch_id`),
  CONSTRAINT `fk_user_branch` FOREIGN KEY (`branch_id`) REFERENCES `branches` (`branch_id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin','admin123','SUPER_ADMIN','ACTIVE',NULL),(2,'head_delhi','1234','BRANCH_HEAD','ACTIVE',1),(3,'head_mumbai','1234','BRANCH_HEAD','ACTIVE',2),(4,'head_bangalore','1234','BRANCH_HEAD','ACTIVE',3),(5,'head_chandigarh','1234','BRANCH_HEAD','ACTIVE',4),(6,'staff_delhi1','1234','STAFF','ACTIVE',1),(7,'staff_delhi2','1234','STAFF','ACTIVE',1),(8,'staff_mumbai1','1234','STAFF','ACTIVE',2),(9,'staff_bangalore1','1234','STAFF','ACTIVE',3),(10,'staff_chandigarh1','1234','STAFF','ACTIVE',4),(11,'rahul','1234','CUSTOMER','ACTIVE',NULL),(12,'priya','1234','CUSTOMER','ACTIVE',NULL),(13,'amit','1234','CUSTOMER','ACTIVE',NULL),(14,'neha','1234','CUSTOMER','ACTIVE',NULL),(15,'rohan','1234','CUSTOMER','ACTIVE',NULL),(16,'kiran','1234','CUSTOMER','ACTIVE',NULL),(17,'sneha','1234','CUSTOMER','ACTIVE',NULL),(18,'vijay','1234','CUSTOMER','ACTIVE',NULL),(19,'anjali','1234','CUSTOMER','ACTIVE',NULL),(20,'akash','1234','CUSTOMER','ACTIVE',NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `customer_account_view`
--

/*!50001 DROP VIEW IF EXISTS `customer_account_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `customer_account_view` AS select `a`.`account_id` AS `account_id`,`a`.`user_id` AS `user_id`,`b`.`branch_name` AS `branch_name`,`a`.`account_type` AS `account_type`,`a`.`balance` AS `balance`,`a`.`acc_status` AS `acc_status` from (`accounts` `a` join `branches` `b` on((`a`.`branch_id` = `b`.`branch_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `customer_transactions_view`
--

/*!50001 DROP VIEW IF EXISTS `customer_transactions_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `customer_transactions_view` AS select `t`.`transaction_id` AS `transaction_id`,`t`.`account_id` AS `account_id`,`t`.`related_account_id` AS `related_account_id`,`t`.`transaction_type` AS `transaction_type`,`t`.`amount` AS `amount`,`t`.`transaction_date_time` AS `transaction_date_time`,`a`.`user_id` AS `user_id` from (`transactions` `t` join `accounts` `a` on((`t`.`account_id` = `a`.`account_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-07-19 14:51:39
