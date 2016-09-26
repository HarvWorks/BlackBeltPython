CREATE DATABASE  IF NOT EXISTS `blackbelt` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `blackbelt`;
-- MySQL dump 10.13  Distrib 5.7.12, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: blackbelt
-- ------------------------------------------------------
-- Server version	5.6.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `date_birth` date DEFAULT NULL,
  `alias` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (14,'Harvey','Chui','c4fusion@gmail.com','$2b$12$wSP6X/Fs2GQZkX2dYAu3U.YKPHG/8R9ONBFygJNb..pS3lZGzpjkW','2016-09-26 10:12:48','2016-09-26 10:12:48','2016-09-04','c4fusion@gmail.com'),(17,'Moo','Cow','mc@poop.com','$2b$12$OJPilAgengmE2/8QU8caZ.qVROeZk4AW6rDQXvRKZ5Stk1mVapWIO','2016-09-26 10:44:27','2016-09-26 10:44:27','2016-09-01','Moo2'),(18,'Matt','Damon','Matt@matt.com','$2b$12$T/dLPWvK4a49sBhteK5SG.QCvvfSR2qJW4GpK6GupELq0rOVMEBf2','2016-09-26 10:45:51','2016-09-26 10:45:51','2016-07-06','The Real Matt'),(19,'Hella','Hella','hella@g.com','$2b$12$zyOf3UmqwVSzxPCfUTv..Ok9WDGagrEObSn77zdBETXPDGNwNZd4m','2016-09-26 10:49:39','2016-09-26 10:49:39','2016-09-06','HellaAwesome'),(20,'Kell','Mih','kell@gmail.com','$2b$12$7qzihX2T2lSV7rzqU/dx/eAcJOp1BbKDfsyUfgReHSF3ygdPY.OSG','2016-09-26 11:40:30','2016-09-26 11:40:30','2016-04-03','ASDSAD'),(21,'Wadf','Kellad','xsafdsf@sfadfa.com','$2b$12$bjs26/jOZq0IDBGJ/NIMAurJIPA4tmrfnnmZ9TY.gPwvgbzjH7vd.','2016-09-26 12:04:27','2016-09-26 12:04:27','2015-10-05','Mesha');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-09-26 12:06:25
