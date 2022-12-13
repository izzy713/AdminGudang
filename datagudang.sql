-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 12, 2022 at 03:59 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

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
('HP01', 'Handphone Samsung A53 8/256GB Done', 5, 4999999, 'o', '2022-11-05', 'adi.sucipt'),
('MNT01', 'Monitor Samsung SR24R350 ', 10, 1799999, 'Y', '2022-10-05', 'adi.sucipto'),
('HP-01', 'Handphone Samsung', 1, 3500000, 'o', '2022-10-27', 'saya'),
('KYB-01', 'Keyboard Logitech', 0, 0, 'o', '2022-10-28', 'saya'),
('abc-03', 'baterai abc 03', 20, 5000, 'o', '2022-11-05', 'Adi'),
('MJ-01', 'Meja Kampus Olympic', 5, 300000, 'Y', '2022-11-09', 'Adi');

-- --------------------------------------------------------

--
-- Table structure for table `logs`
--

CREATE TABLE `logs` (
  `logs_id` int(10) NOT NULL,
  `logs_table` varchar(25) NOT NULL,
  `logs_params` varchar(25) NOT NULL,
  `logs_data` varchar(2000) NOT NULL,
  `logs_cdate` datetime NOT NULL,
  `logs_cuser` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `logs`
--

INSERT INTO `logs` (`logs_id`, `logs_table`, `logs_params`, `logs_data`, `logs_cdate`, `logs_cuser`) VALUES
(1, 'barang', 'insert', 'barang_id = 1&barang_desc = 1&barang_total = 10barang_price = Rp15000&barang_actived = Y&barang_cdate = 11/30/2022, 15:09:46&barang_cuser = ad', '2022-11-30 15:09:46', 'system'),
(2, 'barang', 'update', 'barang_id = 1 &barang_desc = 1 done &barang_total = 10 &barang_price = Rp15000 &barang_actived = Y &barang_cdate = 11/30/2022, 15:12:17 &barang_cuser = ad', '2022-11-30 15:12:17', 'system'),
(3, 'barang', 'delete', 'barang_id = 1', '2022-11-30 15:12:29', 'system'),
(4, 'barang', 'insert', 'barang_id = HKC-91 &barang_desc = Handphone Samsung &barang_total = 5 &barang_price = Rp50000 &barang_actived = Y &barang_cdate = 12/01/2022, 16:57:26 &barang_cuser = Adzka', '2022-12-01 16:57:26', 'system'),
(5, 'barang', 'delete', 'barang_id = HKC-91', '2022-12-02 21:44:52', 'system');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `logs`
--
ALTER TABLE `logs`
  ADD PRIMARY KEY (`logs_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `logs`
--
ALTER TABLE `logs`
  MODIFY `logs_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
