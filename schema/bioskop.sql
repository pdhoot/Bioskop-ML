-- phpMyAdmin SQL Dump
-- version 4.4.13.1deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 03, 2016 at 05:52 PM
-- Server version: 5.6.28-0ubuntu0.15.10.1
-- PHP Version: 5.6.11-1ubuntu3.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bioskop`
--

-- --------------------------------------------------------

--
-- Table structure for table `FEAT_DB`
--

CREATE TABLE IF NOT EXISTS `FEAT_DB` (
  `id` int(10) NOT NULL,
  `features` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `LOGS_DB`
--

CREATE TABLE IF NOT EXISTS `LOGS_DB` (
  `user` int(10) NOT NULL,
  `movie` int(10) NOT NULL,
  `rating` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `MOVIE_DB`
--

CREATE TABLE IF NOT EXISTS `MOVIE_DB` (
  `id` int(10) NOT NULL,
  `movie` varchar(100) NOT NULL,
  `genre` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `PRED_DB`
--

CREATE TABLE IF NOT EXISTS `PRED_DB` (
  `id` int(10) NOT NULL,
  `prediction` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `USER_DB`
--

CREATE TABLE IF NOT EXISTS `USER_DB` (
  `id` int(10) NOT NULL,
  `gender` varchar(1) NOT NULL,
  `age` int(3) NOT NULL,
  `occu` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `FEAT_DB`
--
ALTER TABLE `FEAT_DB`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `MOVIE_DB`
--
ALTER TABLE `MOVIE_DB`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `PRED_DB`
--
ALTER TABLE `PRED_DB`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `USER_DB`
--
ALTER TABLE `USER_DB`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `FEAT_DB`
--
ALTER TABLE `FEAT_DB`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `MOVIE_DB`
--
ALTER TABLE `MOVIE_DB`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `PRED_DB`
--
ALTER TABLE `PRED_DB`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `USER_DB`
--
ALTER TABLE `USER_DB`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
