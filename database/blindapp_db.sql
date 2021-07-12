/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - blindapp
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`thirdeye` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `thirdeye`;

/*Table structure for table `blind` */

DROP TABLE IF EXISTS `blind`;

CREATE TABLE `blind` (
  `blind_id` int(11) NOT NULL AUTO_INCREMENT,
  `cartaker_id` int(11) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `photo` varchar(500) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `Gender` varchar(50) DEFAULT NULL,
  `Dob` varchar(25) DEFAULT NULL,
  `imei` varchar(25) DEFAULT NULL,
  `Latitude` varchar(50) DEFAULT NULL,
  `Longitude` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`blind_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `blind` */

/*Table structure for table `caretaker` */

DROP TABLE IF EXISTS `caretaker`;

CREATE TABLE `caretaker` (
  `care_taker_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(30) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `Email` varchar(40) DEFAULT NULL,
  `log_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`care_taker_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `caretaker` */

/*Table structure for table `emergency_numbers` */

DROP TABLE IF EXISTS `emergency_numbers`;

CREATE TABLE `emergency_numbers` (
  `emergency_number_id` int(11) NOT NULL AUTO_INCREMENT,
  `blind_id` int(11) DEFAULT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `Relation` varchar(30) DEFAULT NULL,
  `Latitude` varchar(40) DEFAULT NULL,
  `Longitude` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`emergency_number_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `emergency_numbers` */

/*Table structure for table `faces` */

DROP TABLE IF EXISTS `faces`;

CREATE TABLE `faces` (
  `face_id` int(11) NOT NULL AUTO_INCREMENT,
  `blind_id` int(11) DEFAULT NULL,
  `person_first_name` varchar(50) DEFAULT NULL,
  `person_last_name` varchar(50) DEFAULT NULL,
  `Date_time` varchar(50) DEFAULT NULL,
  `relation` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`face_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `faces` */

/*Table structure for table `help` */

DROP TABLE IF EXISTS `help`;

CREATE TABLE `help` (
  `help_id` int(11) NOT NULL AUTO_INCREMENT,
  `blind_id` int(11) DEFAULT NULL,
  `Datetime` varchar(50) DEFAULT NULL,
  `request_status` varchar(50) DEFAULT NULL,
  `Latitude` varchar(50) DEFAULT NULL,
  `Longitude` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`help_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `help` */

/*Table structure for table `location` */

DROP TABLE IF EXISTS `location`;

CREATE TABLE `location` (
  `location_id` int(11) NOT NULL AUTO_INCREMENT,
  `blind_id` int(11) DEFAULT NULL,
  `Latitude` varchar(50) DEFAULT NULL,
  `Longitude` varchar(50) DEFAULT NULL,
  `Datetime` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`location_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `location` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`log_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`log_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin');



DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `blind_id` int(11) DEFAULT NULL,
  `message_description` varchar(100) DEFAULT NULL,
  `Reply_description` varchar(100) DEFAULT NULL,
  `Datetime` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
