-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 28, 2022 at 05:31 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `datagudang`
--

-- --------------------------------------------------------

--
-- Table structure for table `barang`
--

CREATE TABLE `barang` (
  `barang_id` varchar(10) NOT NULL COMMENT 'ID barang',
  `barang_desc` varchar(255) NOT NULL COMMENT 'Deskripsi Barang',
  `barang_total` int(10) NOT NULL COMMENT 'jumlah barang',
  `barang_price` int(11) NOT NULL COMMENT 'Harga Barang',
  `barang_actived` char(1) NOT NULL COMMENT 'Status barang saat ini aktif atau tidak (Y/N)',
  `barang_cdate` date NOT NULL COMMENT 'Tanggal input barang (Create Date)',
  `barang_cuser` varchar(20) NOT NULL COMMENT 'User yang menginput data barang (Create user)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Table pendataan barang';

--
-- Dumping data for table `barang`
--

INSERT INTO `barang` (`barang_id`, `barang_desc`, `barang_total`, `barang_price`, `barang_actived`, `barang_cdate`, `barang_cuser`) VALUES
('LTP01', 'Laptop Thinkpad E490', 2, 12000000, 'Y', '2022-10-05', 'adi.sucipt'),
('HP01', 'Handphone Samsung A53 8/256GB', 5, 4999999, 'Y', '2022-10-05', 'adi.sucipt'),
('MNT01', 'Monitor Samsung SR24R350 ', 10, 1799999, 'Y', '2022-10-05', 'adi.sucipto'),
('MTR-01', 'Motor Beat Street 2021', 1, 17000000, 'o', '2022-10-26', 'saya'),
('MTR-01', 'Motor Beat Street 2021', 1, 17000000, 'o', '2022-10-26', 'saya'),
('MTR-01', 'Motor Beat Street 2021', 1, 123, 'o', '2022-10-27', 'saya'),
('MTR-01', 'Motor Beat Street 2021', 1, 123, 'o', '2022-10-27', 'saya'),
('HP-01', 'Handphone Samsung', 1, 3500000, 'o', '2022-10-27', 'saya'),
('KYB-01', 'Keyboard Logitech', 0, 0, 'o', '2022-10-28', 'saya');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
