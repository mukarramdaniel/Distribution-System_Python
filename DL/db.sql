-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: dbarm
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `attendence`
--

DROP TABLE IF EXISTS `attendence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attendence` (
  `userName` varchar(45) NOT NULL,
  `name` varchar(45) NOT NULL,
  `date` varchar(45) NOT NULL,
  `id` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendence`
--

LOCK TABLES `attendence` WRITE;
/*!40000 ALTER TABLE `attendence` DISABLE KEYS */;
INSERT INTO `attendence` VALUES ('ammadaslam07@gmail.com','ammad','2022-12-20','20202021'),('mukarramali623@gmail.com','John','2022-12-20','20202022'),('ammadaslam07@gmail.com','ammad','2022-12-21','20202033');
/*!40000 ALTER TABLE `attendence` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `userID` int NOT NULL,
  `userName` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `userRole` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `age` int NOT NULL,
  `contactNum` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Cnic` varchar(45) NOT NULL,
  `bankAccount` varchar(45) NOT NULL,
  `salary` varchar(45) DEFAULT NULL,
  `created_on` varchar(45) NOT NULL,
  `update_on` varchar(45) NOT NULL,
  `dateTime` varchar(45) NOT NULL,
  `Salary_Status` int NOT NULL,
  PRIMARY KEY (`userID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (2,'mukarramali623@gmail.com','employee12345',1,'John',34,'03157963703','mukarramali623@gmail.com','3130258066436','435545345454','30000','15-01-2022 08:15:11','15-01-2022 08:15:11','15-01-2022 08:15:11',1),(3,'ammadaslam1997@gmail.com','employee123',2,'AMMAD',22,'03129250987','ammadaslam1997@gmail.com','3510266901853','434343443434','100000','12-01-2022 08:15:11','12-01-2022 08:15:11','15-01-2022 08:15:11',0);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory` (
  `prodCategory` varchar(45) NOT NULL,
  `buyPrice` float NOT NULL,
  `profitMargin` float DEFAULT NULL,
  `shoeSize` float NOT NULL,
  `selPrice` float DEFAULT NULL,
  `color` varchar(45) NOT NULL,
  `prodID` int NOT NULL,
  `type` varchar(45) NOT NULL,
  PRIMARY KEY (`prodID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES ('Joggers',3000,35,8,3035,'black',1,'male'),('sandles',3100,40,9,NULL,'brown',2,'female');
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manager`
--

DROP TABLE IF EXISTS `manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manager` (
  `userID` int NOT NULL,
  `userName` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `userRole` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `age` varchar(45) NOT NULL,
  `contactNum` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Cnic` varchar(45) NOT NULL,
  `bankAccount` varchar(45) NOT NULL,
  `resetToken` varchar(45) DEFAULT NULL,
  `created_on` varchar(45) NOT NULL,
  `update_on` varchar(45) NOT NULL,
  PRIMARY KEY (`userID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manager`
--

LOCK TABLES `manager` WRITE;
/*!40000 ALTER TABLE `manager` DISABLE KEYS */;
INSERT INTO `manager` VALUES (1,'rasheedrayan514@gmail.com','admin12345',0,'Rayan Rasheed','40','03157963703','rasheedrayan514@gmail.com','3130258066437','102934848943834','12345678','10-12-2022','10-12-2022');
/*!40000 ALTER TABLE `manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rider`
--

DROP TABLE IF EXISTS `rider`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rider` (
  `userID` int NOT NULL,
  `userName` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `userRole` varchar(45) NOT NULL,
  `name` varchar(45) NOT NULL,
  `age` varchar(45) NOT NULL,
  `contactNum` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Cnic` varchar(45) NOT NULL,
  `bankAccount` varchar(45) NOT NULL,
  `resetToken` varchar(45) NOT NULL,
  `created_on` varchar(45) NOT NULL,
  `updated_on` varchar(45) NOT NULL,
  `time` varchar(45) DEFAULT NULL,
  `latitude` float DEFAULT NULL,
  `longitutde` float DEFAULT NULL,
  `fieldArea` varchar(45) DEFAULT NULL,
  `VehicleNumber` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`userID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rider`
--

LOCK TABLES `rider` WRITE;
/*!40000 ALTER TABLE `rider` DISABLE KEYS */;
/*!40000 ALTER TABLE `rider` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shop`
--

DROP TABLE IF EXISTS `shop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `shop` (
  `riderID` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `Cnic` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `latitude` float NOT NULL,
  `longitude` float NOT NULL,
  `address` varchar(300) NOT NULL,
  `phoneNum` varchar(45) NOT NULL,
  `accountNo` varchar(45) NOT NULL,
  `FieldArea` varchar(45) NOT NULL,
  `shopName` varchar(45) NOT NULL,
  `timeOpen` varchar(45) NOT NULL,
  `timeClose` varchar(45) NOT NULL,
  PRIMARY KEY (`Cnic`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shop`
--

LOCK TABLES `shop` WRITE;
/*!40000 ALTER TABLE `shop` DISABLE KEYS */;
INSERT INTO `shop` VALUES (4,'Umer Jamil','3130260006145','hasannawaz2486@gmail.com',31.4105,73.1028,'Abdul Haque Rd, Trade Centre Commercial Area Phase 2 Johar Town, Lahore, Punjab 54000, Pakistan','03166668888','062341671898','Johar Town','Shoe Planet','11:00 AM','11:00 PM'),(4,'Hassan Nawaz','3130260006183','hasannawaz2486@gmail.com',3146730,74.2663,'Abdul Haque Rd, Trade Centre Commercial Area Phase 2 Johar Town, Lahore, Punjab 54000, Pakistan','03166668888','062341671898','Johar Town','Shoe Mela','11:00 AM','11:00 PM');
/*!40000 ALTER TABLE `shop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `spare`
--

DROP TABLE IF EXISTS `spare`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `spare` (
  `prodCategory` varchar(45) NOT NULL,
  `buyPrice` int NOT NULL,
  `profiMargin` int DEFAULT NULL,
  `shoeSize` float NOT NULL,
  `sellPrice` int DEFAULT NULL,
  `color` varchar(45) NOT NULL,
  `prodID` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `spare`
--

LOCK TABLES `spare` WRITE;
/*!40000 ALTER TABLE `spare` DISABLE KEYS */;
INSERT INTO `spare` VALUES ('Pumpy',3050,130,8,3180,'black',0),('Joggers',2090,120,9,2210,'brown',0);
/*!40000 ALTER TABLE `spare` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stock_order_crud`
--

DROP TABLE IF EXISTS `stock_order_crud`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stock_order_crud` (
  `prodCategory` varchar(45) NOT NULL,
  `buyPrice` float DEFAULT NULL,
  `profitMargin` float DEFAULT NULL,
  `shoeSize` float NOT NULL,
  `selPrice` float DEFAULT NULL,
  `color` varchar(45) NOT NULL,
  `prodID` int NOT NULL,
  `type` varchar(45) NOT NULL,
  `orderID` int NOT NULL,
  `date` varchar(45) NOT NULL,
  `status` int DEFAULT NULL,
  PRIMARY KEY (`prodID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stock_order_crud`
--

LOCK TABLES `stock_order_crud` WRITE;
/*!40000 ALTER TABLE `stock_order_crud` DISABLE KEYS */;
INSERT INTO `stock_order_crud` VALUES ('Joggers',1050,30,8,1080,'black',3452,'male',1,'22-05-2022 11:05:04',1),('Pummpy',1030,20,9,1090,'brown',4233,'male',1,'22-05-2022 11:05:04',1),('Joggers',1220,30,9,1080,'black',4256,'male',2,'22-05-2022 11:05:04',1);
/*!40000 ALTER TABLE `stock_order_crud` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `userID` int NOT NULL,
  `userName` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `userRole` varchar(45) NOT NULL,
  `name` varchar(256) NOT NULL,
  `age` int NOT NULL,
  `contactNum` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `CNIC` varchar(45) NOT NULL,
  `BankAccount` varchar(45) NOT NULL,
  `createdDate` varchar(45) NOT NULL,
  `updatedDate` varchar(45) NOT NULL,
  PRIMARY KEY (`userID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'rasheedrayan@gmailcom','123','0','Rayan Rasheed',18,'03077963751','rasheedrayan514@gmail.com','3130258066437','043227118332','12112022','13112021');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vehicle`
--

DROP TABLE IF EXISTS `vehicle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vehicle` (
  `model` varchar(45) NOT NULL,
  `number` varchar(45) NOT NULL,
  `fuelAverage` float NOT NULL,
  `riderID` int NOT NULL,
  PRIMARY KEY (`number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vehicle`
--

LOCK TABLES `vehicle` WRITE;
/*!40000 ALTER TABLE `vehicle` DISABLE KEYS */;
INSERT INTO `vehicle` VALUES ('2018','AL2022',9,2),('2017','AL3099',10,1);
/*!40000 ALTER TABLE `vehicle` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-20 15:31:39
