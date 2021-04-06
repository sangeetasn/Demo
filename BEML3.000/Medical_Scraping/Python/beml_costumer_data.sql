-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: beml
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
-- Table structure for table `costumer_data`
--

DROP TABLE IF EXISTS `costumer_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `costumer_data` (
  `Reference_Number` varchar(30) NOT NULL,
  `Date` varchar(45) NOT NULL,
  `Staff_Number` int(11) NOT NULL,
  `Staff_Name` varchar(45) NOT NULL,
  `Patient_Name` varchar(45) NOT NULL,
  `Patient_Relationship` varchar(45) NOT NULL,
  `Hospital_Name` varchar(45) NOT NULL,
  `Hospital_Adrdress` varchar(45) NOT NULL,
  `Reason_For_Hospitality` varchar(45) NOT NULL,
  `Signature` varchar(45) DEFAULT NULL,
  `Patient_Photo` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `costumer_data`
--

LOCK TABLES `costumer_data` WRITE;
/*!40000 ALTER TABLE `costumer_data` DISABLE KEYS */;
INSERT INTO `costumer_data` VALUES ('KPM/Refltr/27302','2021-01-11',27302,'Vijaylaxmi','savita','Mother','Bangalore','Fortis Hospital','covid','Ashish Signature.png','kamala.jpg'),('KPM/Refltr/27302','2021-01-12',27302,'Nayana','savita','Mother','Bangalore','Fortis Hospital','covid','Rajshekar signature.png','kamala.jpg');
/*!40000 ALTER TABLE `costumer_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-01-12 10:20:28
