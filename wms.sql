-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: wms
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `admin_login`
--

DROP TABLE IF EXISTS `admin_login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin_login` (
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_login`
--

LOCK TABLES `admin_login` WRITE;
/*!40000 ALTER TABLE `admin_login` DISABLE KEYS */;
INSERT INTO `admin_login` VALUES ('omkar28','123');
/*!40000 ALTER TABLE `admin_login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_details`
--

DROP TABLE IF EXISTS `employee_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_details` (
  `employee_id` int NOT NULL AUTO_INCREMENT,
  `employee_name` char(45) NOT NULL,
  `profession` varchar(20) NOT NULL,
  `date_of_joining` varchar(20) NOT NULL,
  `contact_no` varchar(10) NOT NULL,
  `emergency_contact_no` varchar(10) NOT NULL,
  `username` varchar(10) DEFAULT NULL,
  `project` tinytext,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_details`
--

LOCK TABLES `employee_details` WRITE;
/*!40000 ALTER TABLE `employee_details` DISABLE KEYS */;
INSERT INTO `employee_details` VALUES (1,'Omkar','Engineer','28/02/2005','9136898004','8169570160','asdf123','[1,2,3]'),(2,'Jayesh','Administrator','29/05/2004','1234567891','9874561231','jayesh24','[2,3,4]'),(3,'Chetan','Engineer','30/06/2005','5467891231','5467895461','chetan12','[3,4]'),(4,'Omkar','Engineer','12/01/2012','9136898004','4561237984','omkar28','[1,2]'),(5,'asdfg','Administrator','28/02/2004','1234567891','1234567891','omkar456',NULL),(6,'Pushkar','Engineer','17/05/2004','6547891234','4569871231','pushkar234',NULL),(7,'Omkar','Administrator','28/02/2005','4567894564','3213214564','pushkar54',NULL),(10,'Pushkar','Management','28/02/2005','9136898004','8169570160','radsa',NULL),(13,'chetan','Engenieer','2024-4-20','4512785623','1245785623','chetan45',NULL),(28,'harsh','Management','2024-04-20','1234567891','8794561230','harsh123',NULL),(29,'roshan','Administrator','2024-04-20','3124568975','6548791234','roshan123',NULL),(30,'rajesh','Administrator','2024-04-24','1554658575','1547586954','rajesh12',NULL);
/*!40000 ALTER TABLE `employee_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project` (
  `unique_id` int NOT NULL AUTO_INCREMENT,
  `project_name` varchar(45) DEFAULT NULL,
  `start_date` varchar(10) DEFAULT NULL,
  `due_date` varchar(10) DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  `total_tasks` tinytext,
  `tasks_done` tinytext,
  `description` mediumtext,
  `participants` tinytext,
  `tasks` tinytext,
  PRIMARY KEY (`unique_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
INSERT INTO `project` VALUES (1,'Library Managemnet','28/02/2025','28/02/2026','omkar28','5','2','This project is about the managing a library and creating  a system .',NULL,NULL),(2,'Workspace','31/03/2023','31/08/2023','jayes12','10','5','This project is about workspace. ',NULL,NULL),(3,'Whatsapp Clone','20/05/2019','21/03/2020','chetan24','8','3','This project is about the cloning the whatsapplication.',NULL,NULL),(4,'Banking System','2024-04-27','20/02/2024',NULL,'36','0','This project is to perform all banking operations\n','[1, 2, 3]','[11, 12, 13'),(5,'Clone','2024-04-27','25/02/2025',NULL,'35','0','This project helps to clone objects\n','[1, 2, 3]','[12, 13, 10]'),(6,'Flappy Bird','2024-04-27','25/02/2020',NULL,'34','0','Bird flying game\n','[1, 2, 3]','[10, 12, 12]'),(7,'Chat Bot','2024-04-27','28/02/2021',NULL,'22','0','This project helps to fetch all information about given prompt in text format\n','[2, 3]','[10, 12]'),(8,'anydesk','2024-04-27','21/02/2025',NULL,'20','0','to access remote window \n','[1, 2]','[10, 10]'),(9,'pycharm','2024-04-27','21/02/2026',NULL,'22','0','code editor\n','[1, 2, 3]','[10, 5, 7]'),(10,'chat','2024-04-27','28/02/2023',NULL,'36','0','chatting application\n','[2, 3, 4]','[11, 12, 13]'),(11,'xyx','2024-04-27','12/02/2023',NULL,'35','0','sdadad\n','[3, 4, 5]','[10, 12, 13]');
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_details`
--

DROP TABLE IF EXISTS `project_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project_details` (
  `project_id` int DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  `total_task` int DEFAULT NULL,
  `working_task` int DEFAULT NULL,
  `color` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_details`
--

LOCK TABLES `project_details` WRITE;
/*!40000 ALTER TABLE `project_details` DISABLE KEYS */;
INSERT INTO `project_details` VALUES (1,'omkar28',10,2,'red'),(2,'omkar28',20,13,'blue'),(1,'chetan45',15,6,'yellow');
/*!40000 ALTER TABLE `project_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `request_login`
--

DROP TABLE IF EXISTS `request_login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `request_login` (
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `request_login`
--

LOCK TABLES `request_login` WRITE;
/*!40000 ALTER TABLE `request_login` DISABLE KEYS */;
INSERT INTO `request_login` VALUES ('chetan45','1236'),('jayesh145','1452'),('ramesh21','4567');
/*!40000 ALTER TABLE `request_login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `requests`
--

DROP TABLE IF EXISTS `requests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `requests` (
  `request_id` int NOT NULL AUTO_INCREMENT,
  `employee_name` varchar(45) NOT NULL,
  `profession` varchar(45) NOT NULL,
  `contact_no` varchar(45) NOT NULL,
  `emergency_contact_no` varchar(45) NOT NULL,
  `username` varchar(45) NOT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `requests`
--

LOCK TABLES `requests` WRITE;
/*!40000 ALTER TABLE `requests` DISABLE KEYS */;
INSERT INTO `requests` VALUES (2,'jayesh','Engineer','1234567890','1234567890','jayesh145'),(6,'ramesh','Engineer','5154565454','9874547454','ramesh21');
/*!40000 ALTER TABLE `requests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `salary`
--

DROP TABLE IF EXISTS `salary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `salary` (
  `employee_id` int NOT NULL AUTO_INCREMENT,
  `employee_name` varchar(45) NOT NULL,
  `profession` varchar(20) NOT NULL,
  `hourly_salary` varchar(20) NOT NULL,
  `working_hours` varchar(20) DEFAULT NULL,
  `salary` varchar(20) DEFAULT NULL,
  `username` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `salary`
--

LOCK TABLES `salary` WRITE;
/*!40000 ALTER TABLE `salary` DISABLE KEYS */;
INSERT INTO `salary` VALUES (1,'Omkar','Engineer','400','6.0','400.0','asdf123'),(2,'Jayesh','Administrator','300','4.0','850.0','jayesh24'),(3,'Chetan','Engineer','400','2.0','600.0','chetan12'),(4,'jayhesh','Engineer','400','998','400.0','omkar28'),(5,'asdfg','Administrator','300','2.0','600.0','omkar456'),(6,'Pushkar','Engineer','400','3.0','1200.0','pushkar234'),(7,'Omkar','Administrator','300','1.0','300.0','pushkar54'),(8,'Pushkar','Management','500','2.0','1000.0','radsa');
/*!40000 ALTER TABLE `salary` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_login`
--

DROP TABLE IF EXISTS `user_login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_login` (
  `username` varchar(10) NOT NULL,
  `password` varchar(10) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_login`
--

LOCK TABLES `user_login` WRITE;
/*!40000 ALTER TABLE `user_login` DISABLE KEYS */;
INSERT INTO `user_login` VALUES ('ankit29','2323'),('asdf123','1231'),('chetan12','2802'),('harsh123','12345'),('harshvar','1234'),('jayesh12','1200'),('jayesh24','1324'),('omkar28','1234'),('omkar456','2343'),('pushkar234','2342'),('pushkar54','2323'),('radsa','1230'),('rajesh12','6541'),('roshan123','4566');
/*!40000 ALTER TABLE `user_login` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-27 20:37:36
