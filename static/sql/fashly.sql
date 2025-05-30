-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 25-05-2025 a las 19:25:58
-- Versión del servidor: 8.0.41
-- Versión de PHP: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `fashly`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carritto`
--

CREATE TABLE `carritto` (
  `id` int NOT NULL,
  `producto_id` int NOT NULL,
  `usuario_id` int NOT NULL,
  `pedidos_id` int DEFAULT NULL,
  `cantidad` int NOT NULL DEFAULT '1',
  `importe` float NOT NULL,
  `status` char(1) NOT NULL DEFAULT 'T'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `catalogos`
--

CREATE TABLE `catalogos` (
  `id` int NOT NULL,
  `nombre` text NOT NULL,
  `tipo` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedidos`
--

CREATE TABLE `pedidos` (
  `id` int NOT NULL,
  `usuario_id` int NOT NULL,
  `total` int NOT NULL,
  `fecha` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id` int NOT NULL,
  `nombre` text NOT NULL,
  `precio` float NOT NULL,
  `descripcion` text NOT NULL,
  `catalogo_id` int NOT NULL,
  `nombre_imagen` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Volcado de datos para la tabla `productos`
--

INSERT INTO `productos` (`id`, `nombre`, `precio`, `descripcion`, `catalogo_id`, `nombre_imagen`) VALUES
(1, 'Camisa Azul', 25.99, 'Camisa Azul de alta calidad.', 101, 'camisa_azul.jpg'),
(2, 'Pantalón Negro', 39.99, 'Pantalón Negro de alta calidad.', 101, 'pantalon_negro.jpg'),
(3, 'Zapatillas Blancas', 49.99, 'Zapatillas Blancas de alta calidad.', 101, 'zapatillas_blancas.jpg'),
(4, 'Falda Roja', 29.99, 'Falda Roja de alta calidad.', 101, 'falda_roja.jpg'),
(5, 'Chaqueta de Cuero', 69.99, 'Chaqueta de Cuero de alta calidad.', 101, 'chaqueta_de_cuero.jpg'),
(6, 'Camiseta Gris', 19.99, 'Camiseta Gris de alta calidad.', 101, 'camiseta_gris.jpg'),
(7, 'Gafas de Sol', 14.99, 'Gafas de Sol de alta calidad.', 101, 'gafas_de_sol.jpg'),
(8, 'Bolso Negro', 39.99, 'Bolso Negro de alta calidad.', 101, 'bolso_negro.jpg'),
(9, 'Cinturón Marrón', 9.99, 'Cinturón Marrón de alta calidad.', 101, 'cinturon_marron.jpg'),
(10, 'Reloj Digital', 29.99, 'Reloj Digital de alta calidad.', 101, 'reloj_digital.jpg'),
(11, 'Camisa Blanco', 25.99, 'Camisa Blanco de alta calidad.', 101, 'camisa_blanco.jpg'),
(12, 'Pantalón Azul', 39.99, 'Pantalón Azul de alta calidad.', 101, 'pantalon_azul.jpg'),
(13, 'Zapatillas Negras', 49.99, 'Zapatillas Negras de alta calidad.', 101, 'zapatillas_negras.jpg'),
(14, 'Falda Gris', 29.99, 'Falda Gris de alta calidad.', 101, 'falda_gris.jpg'),
(15, 'Chaqueta Roja', 69.99, 'Chaqueta Roja de alta calidad.', 101, 'chaqueta_roja.jpg'),
(16, 'Camiseta Azul', 19.99, 'Camiseta Azul de alta calidad.', 101, 'camiseta_azul.jpg'),
(17, 'Gafas Marrón', 14.99, 'Gafas Marrón de alta calidad.', 101, 'gafas_marron.jpg'),
(18, 'Bolso Blanco', 39.99, 'Bolso Blanco de alta calidad.', 101, 'bolso_blanco.jpg'),
(19, 'Cinturón Negro', 9.99, 'Cinturón Negro de alta calidad.', 101, 'cinturon_negro.jpg'),
(20, 'Reloj Analógico', 29.99, 'Reloj Analógico de alta calidad.', 101, 'reloj_analogico.jpg'),
(21, 'Camisa Roja', 25.99, 'Camisa Roja de alta calidad.', 101, 'camisa_roja.jpg'),
(22, 'Pantalón Gris', 39.99, 'Pantalón Gris de alta calidad.', 101, 'pantalon_gris.jpg'),
(23, 'Zapatillas Azules', 49.99, 'Zapatillas Azules de alta calidad.', 101, 'zapatillas_azules.jpg'),
(24, 'Falda Marrón', 29.99, 'Falda Marrón de alta calidad.', 101, 'falda_marron.jpg'),
(25, 'Chaqueta Negra', 69.99, 'Chaqueta Negra de alta calidad.', 101, 'chaqueta_negra.jpg'),
(26, 'Camiseta Blanca', 19.99, 'Camiseta Blanca de alta calidad.', 101, 'camiseta_blanca.jpg'),
(27, 'Gafas Azules', 14.99, 'Gafas Azules de alta calidad.', 101, 'gafas_azules.jpg'),
(28, 'Bolso Rojo', 39.99, 'Bolso Rojo de alta calidad.', 101, 'bolso_rojo.jpg'),
(29, 'Cinturón Gris', 9.99, 'Cinturón Gris de alta calidad.', 101, 'cinturon_gris.jpg'),
(30, 'Reloj Digital Negro', 29.99, 'Reloj Digital Negro de alta calidad.', 101, 'reloj_digital_negro.jpg'),
(31, 'Chamarra Negra', 25.99, 'chamarra Negra de alta calidad.', 101, 'camisa_negra.jpg'),
(32, 'Pantalón Blanco', 39.99, 'Pantalón Blanco de alta calidad.', 101, 'pantalon_blanco.jpg'),
(33, 'Zapatillas Rojas', 49.99, 'Zapatillas Rojas de alta calidad.', 101, 'zapatillas_rojas.jpg'),
(34, 'Falda Azul', 29.99, 'Falda Azul de alta calidad.', 101, 'falda_azul.jpg'),
(35, 'Chaqueta Blanca', 69.99, 'Chaqueta Blanca de alta calidad.', 101, 'chaqueta_blanca.jpg'),
(36, 'Camiseta Negra', 19.99, 'Camiseta Negra de alta calidad.', 101, 'camiseta_negra.jpg'),
(37, 'Gafas Negras', 14.99, 'Gafas Negras de alta calidad.', 101, 'gafas_negras.jpg'),
(38, 'Bolso Azul', 39.99, 'Bolso Azul de alta calidad.', 101, 'bolso_azul.jpg'),
(39, 'Cinturón Blanco', 9.99, 'Cinturón Blanco de alta calidad.', 101, 'cinturon_blanco.jpg'),
(40, 'Reloj Analógico Blanco', 29.99, 'Reloj Analógico Blanco de alta calidad.', 101, 'reloj_analogico_blanco.jpg'),
(41, 'Camisa Gris', 25.99, 'Camisa Gris de alta calidad.', 101, 'camisa_gris.jpg'),
(42, 'Pantalón Marrón', 39.99, 'Pantalón Marrón de alta calidad.', 101, 'pantalon_marron.jpg'),
(43, 'Zapatillas Grises', 49.99, 'Zapatillas Grises de alta calidad.', 101, 'zapatillas_grises.jpg'),
(44, 'Falda Blanca', 29.99, 'Falda Blanca de alta calidad.', 101, 'falda_blanca.jpg'),
(45, 'Chaqueta Azul', 69.99, 'Chaqueta Azul de alta calidad.', 101, 'chaqueta_azul.jpg'),
(46, 'Camiseta Marrón', 19.99, 'Camiseta Marrón de alta calidad.', 101, 'camiseta_marron.jpg'),
(47, 'Gafas Grises', 14.99, 'Gafas Grises de alta calidad.', 101, 'gafas_grises.jpg'),
(48, 'Bolso Gris', 39.99, 'Bolso Gris de alta calidad.', 101, 'bolso_gris.jpg'),
(49, 'Cinturón Azul', 9.99, 'Cinturón Azul de alta calidad.', 101, 'cinturon_azul.jpg'),
(50, 'Reloj Digital Azul', 29.99, 'Reloj Digital Azul de alta calidad.', 101, 'reloj_digital_azul.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int NOT NULL,
  `nombre` varchar(50) CHARACTER SET utf32 COLLATE utf32_spanish_ci NOT NULL,
  `apellido` varchar(50) CHARACTER SET utf32 COLLATE utf32_spanish_ci NOT NULL,
  `correo` varchar(100) CHARACTER SET utf32 COLLATE utf32_spanish_ci NOT NULL,
  `clave` varchar(250) CHARACTER SET utf32 COLLATE utf32_spanish_ci NOT NULL,
  `telefono` varchar(15) CHARACTER SET utf32 COLLATE utf32_spanish_ci NOT NULL,
  `fechareg` datetime NOT NULL,
  `perfil` char(1) CHARACTER SET utf32 COLLATE utf32_spanish_ci NOT NULL DEFAULT 'C'
) ENGINE=InnoDB DEFAULT CHARSET=utf32 COLLATE=utf32_spanish_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `nombre`, `apellido`, `correo`, `clave`, `telefono`, `fechareg`, `perfil`) VALUES
(1, 'Alfonsos', 'garcia', 'jose.garcia2813@alumnos.udg.mx', 'scrypt:32768:8:1$ESYX4cN6UlHb0BkS$e210f75f72229438a17e30b67c260ece7a8f23f0256d8c1dc75950610ccfeb458dfc79f61865425f3715e79da61ea3f70e0e88e24b135e5e70035b8ff5c2f8de', '3310539464', '2025-05-18 13:24:13', 'A'),
(7, 'rogelio pepe', 'de skibidi', 'diego.gonzalez2802@alumnos.udg.mx', 'scrypt:32768:8:1$6MldeZevzFCprg30$6cff265ab7afabb6469a6d6d859542a8c7674a27a997187953aa65a1da2aa1d750c887b3d2fe3f828d0e8d670d6b1116bcfb5a932275e4e3a07b3f140f5d35a1', '3312634983', '2025-02-27 17:38:06', 'C'),
(8, 'Alfonso', 'Franco', 'adan.lopez6589@academicos.udg.mx', 'scrypt:32768:8:1$KRWdqSobrv5RNCGa$151c0a439fd960931fd3679730e32a30eb5ca1e51a1e0a9d6ce4327856cc0d478c602177a083531e5d14d800903455220d49b7e13b756eacbf848a73f0737979', '3312634983', '2025-03-06 16:59:46', 'C'),
(9, 'gael', 'sexo', 'gaelsexo123@gmail.com', 'scrypt:32768:8:1$YtgwZ1FR9CotNtex$dea5fa5f6edc833083f50ed0ada783222749a1aadbdccc8f947cda25d9976ae2a5c5e5516f4e9862487f99562c2a028855c483b914e794ffcfe5ef477f9fec60', '3329384758', '2025-05-15 22:01:40', 'C'),
(10, 'ALE', 'ALESITA', 'ales2034@gmail.com', 'scrypt:32768:8:1$WC1qYtIaw5R8sINy$69cac8a878fc6fdbfa280edfc5741effbbadf7993fea6f0d01539ab30311158b0f4ce8a9214bae5101aa9ec04485b4dedb947b3bc29fe985ce023a6eb40ebf0c', '3324765809', '2025-05-25 13:24:59', 'A');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `carritto`
--
ALTER TABLE `carritto`
  ADD PRIMARY KEY (`id`),
  ADD KEY `producto_id` (`producto_id`),
  ADD KEY `usuario_id` (`usuario_id`),
  ADD KEY `pedidos_id` (`pedidos_id`);

--
-- Indices de la tabla `catalogos`
--
ALTER TABLE `catalogos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `usuario_id` (`usuario_id`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `catalogo_id` (`catalogo_id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `correo` (`correo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `carritto`
--
ALTER TABLE `carritto`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=282;

--
-- AUTO_INCREMENT de la tabla `catalogos`
--
ALTER TABLE `catalogos`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `pedidos`
--
ALTER TABLE `pedidos`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `carritto`
--
ALTER TABLE `carritto`
  ADD CONSTRAINT `carritto_ibfk_1` FOREIGN KEY (`producto_id`) REFERENCES `productos` (`id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `carritto_ibfk_2` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`) ON UPDATE CASCADE;

--
-- Filtros para la tabla `pedidos`
--
ALTER TABLE `pedidos`
  ADD CONSTRAINT `pedidos_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
