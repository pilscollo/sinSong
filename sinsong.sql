-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 12-03-2022 a las 17:55:06
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sinsong`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `band`
--

CREATE TABLE `band` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `band`
--

INSERT INTO `band` (`id`, `name`, `type`) VALUES
(1, '0', '0'),
(2, 'twice', 'kpop'),
(3, 'itzy', 'kpop');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `song`
--

CREATE TABLE `song` (
  `id` int(11) NOT NULL,
  `link` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `song`
--

INSERT INTO `song` (`id`, `link`, `name`) VALUES
(6, 'https://www.youtube.com/watch?v=3OtGm1aM6gQ', 'album'),
(10, 'https://www.youtube.com/watch?v=2zZxNpzqcAc&list=RDGMEMCMFH2exzjBeE_zAHHJOdxg&start_radio=1&rv=3OtGm', 'feel special'),
(11, 'alknads', 'asdlk'),
(12, 'asd', 'ads'),
(13, 'https://www.youtube.com/watch?v=w4nihuYVTW0&list=RDGMEMCMFH2exzjBeE_zAHHJOdxg&index=3', 'what is love'),
(14, 'https://www.youtube.com/watch?v=nTQgVDB7VOA&list=RDGMEMCMFH2exzjBeE_zAHHJOdxg&index=7', 'notshy');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `union`
--

CREATE TABLE `union` (
  `idsong` int(11) NOT NULL,
  `idband` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `union`
--

INSERT INTO `union` (`idsong`, `idband`) VALUES
(6, 1),
(10, 1),
(11, 1),
(12, 1),
(13, 2),
(14, 3);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `band`
--
ALTER TABLE `band`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `song`
--
ALTER TABLE `song`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `union`
--
ALTER TABLE `union`
  ADD KEY `idsong` (`idsong`),
  ADD KEY `idband` (`idband`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `band`
--
ALTER TABLE `band`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `song`
--
ALTER TABLE `song`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `union`
--
ALTER TABLE `union`
  ADD CONSTRAINT `union_ibfk_1` FOREIGN KEY (`idsong`) REFERENCES `song` (`id`),
  ADD CONSTRAINT `union_ibfk_2` FOREIGN KEY (`idband`) REFERENCES `band` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
