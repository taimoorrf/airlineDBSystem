-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: localhost    Database: airline_management_system
-- ------------------------------------------------------
-- Server version	8.0.18

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
-- Table structure for table `flight_record`
--

DROP TABLE IF EXISTS `flight_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flight_record` (
  `flight_ID` int(11) NOT NULL,
  `departure` varchar(45) NOT NULL,
  `arrival` varchar(45) NOT NULL,
  `airplane_ID` varchar(45) NOT NULL,
  `fare` varchar(45) NOT NULL,
  `depart_time` datetime(4) NOT NULL,
  `arrival_time` datetime(4) NOT NULL,
  PRIMARY KEY (`flight_ID`),
  UNIQUE KEY `flight_ID_UNIQUE` (`flight_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Stores records of all departing and incoming flights.';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight_record`
--

LOCK TABLES `flight_record` WRITE;
/*!40000 ALTER TABLE `flight_record` DISABLE KEYS */;
INSERT INTO `flight_record` VALUES (1,'LHE','KHI','Boeing 223','20,000','2019-03-22 13:01:30.0000','2019-03-22 16:00:00.0000'),(2,'LHE','ISB','Boeing 223','15,000','2019-03-18 23:05:00.0000','2019-03-19 02:00:00.0000'),(3,'LYP','KHI','Boeing 121','28,000','2019-03-25 15:00:00.0000','2019-03-25 17:20:00.0000'),(4,'MUX','PEW','Boeing 878','32,000','2019-03-25 19:00:00.0000','2019-03-25 22:07:00.0000'),(5,'RYK','PEW','Boeing 101','38,000','2019-03-11 09:00:00.0000','2019-03-11 11:45:00.0000'),(6,'MUD','LHE','Boeing 767','42,000','2019-03-28 09:00:00.0000','2019-03-28 11:45:00.0000'),(9,'KHI','LYP','Boeing 612','23,000','2019-04-07 23:30:00.0000','2019-04-08 02:00:00.0000'),(10,'UET','LYP','Boeing 192','33,000','2019-04-12 03:30:00.0000','2019-04-12 05:00:00.0000'),(11,'LHE','UET','Boeing 777','38,000','2019-04-15 23:30:00.0000','2019-04-16 02:15:00.0000'),(12,'LHE','KHI','Boeing 223','25,000','2019-04-21 11:00:00.0000','2019-03-22 14:00:00.0000');
/*!40000 ALTER TABLE `flight_record` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-10-25 22:44:29
