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
-- Table structure for table `passenger_record`
--

DROP TABLE IF EXISTS `passenger_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `passenger_record` (
  `CNIC` varchar(45) NOT NULL,
  `Name` varchar(45) NOT NULL,
  `Contact_Number` varchar(45) NOT NULL,
  `Email_Address` varchar(45) NOT NULL,
  `Address` varchar(225) NOT NULL,
  PRIMARY KEY (`CNIC`),
  UNIQUE KEY `CNIC_UNIQUE` (`CNIC`),
  UNIQUE KEY `Contact_Number_UNIQUE` (`Contact_Number`),
  UNIQUE KEY `Email_Address_UNIQUE` (`Email_Address`) /*!80000 INVISIBLE */
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `passenger_record`
--

LOCK TABLES `passenger_record` WRITE;
/*!40000 ALTER TABLE `passenger_record` DISABLE KEYS */;
INSERT INTO `passenger_record` VALUES ('33100-2334213-7','Usama Tariq','03326646373','usama.tariq@gmail.com','P 25 Hajveri Town Sargodha Road Faisalabad'),('33100-2374887-1','Samee A','03326746131','samee.arif@gmail.com','227-T DHA Phase 2'),('33100-6562661-9','Taimoor Arif','03000995454','taimoorrf@gmail.com','227-T DHA phase 2'),('33100-6787232-9','Ali Iqbal Khan Ghauri','03217723908','alidaddyevil@yahoo.com','ghauri palace'),('33102-6236771-0','Babar Azam','03007231367','betterthankohli@outlook.com','every pakistani\'s heart'),('33198-2041823-9','Bhutto','03337645212','aajbhibhuttozindahai@ppp.com.pk','larrkana'),('33198-2346873-7','Imran Khan Niazi','03002365938','primeminister@gov.com.pk','nashay mein'),('33212-2231883-7','Cristiano Ronaldo','03217764323','messikabeta@yahoo.com','santiago bernabeu'),('33221-6532117-1','Lionel Messi','03221122334','ronaldokapapa@yahoo.com','camp nou'),('33231-6645373-1','Dhakkay kaa','03287645321','random@gmail.com','filler address'),('33231-7667212-3','Abdullah Khan','03031123474','abk@hotmail.com','ghar apnay'),('33231-9823737-0','Nawaz Sharif','03235437834','president@pmln.com.pk','Adiala jail');
/*!40000 ALTER TABLE `passenger_record` ENABLE KEYS */;
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
