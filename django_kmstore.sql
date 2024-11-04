-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 04-11-2024 a las 00:31:10
-- Versión del servidor: 11.5.2-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `django_kmstore`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add producto', 7, 'add_producto'),
(26, 'Can change producto', 7, 'change_producto'),
(27, 'Can delete producto', 7, 'delete_producto'),
(28, 'Can view producto', 7, 'view_producto'),
(29, 'Can add orden envio', 8, 'add_ordenenvio'),
(30, 'Can change orden envio', 8, 'change_ordenenvio'),
(31, 'Can delete orden envio', 8, 'delete_ordenenvio'),
(32, 'Can view orden envio', 8, 'view_ordenenvio'),
(33, 'Can add carrito', 9, 'add_carrito'),
(34, 'Can change carrito', 9, 'change_carrito'),
(35, 'Can delete carrito', 9, 'delete_carrito'),
(36, 'Can view carrito', 9, 'view_carrito'),
(37, 'Can add carrito item', 10, 'add_carritoitem'),
(38, 'Can change carrito item', 10, 'change_carritoitem'),
(39, 'Can delete carrito item', 10, 'delete_carritoitem'),
(40, 'Can view carrito item', 10, 'view_carritoitem');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$720000$ueXvNahdS4v7pqtAPmA12t$c8Kn9sibYnpcaLeiAKHkuUYKVJItM4ggMFbIKeIlPfY=', '2024-11-03 23:28:55.948404', 1, 'brandon', '', '', 'brandon@inacap.com', 1, 1, '2024-11-03 22:51:06.239503'),
(2, 'pbkdf2_sha256$720000$AZw1HLIcGLlNL1LzJzJm4V$4bvNXTfJxrO3EJtlX24tHdY+JAr08dmRkTjRlmTM3R8=', '2024-11-03 23:29:08.377537', 0, 'Ivan', '', '', 'ivan@inacap.cl', 0, 1, '2024-11-03 23:05:28.929458');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-11-03 22:54:29.082289', '1', 'Nike Air Zoom Pegasus 40', 1, '[{\"added\": {}}]', 7, 1),
(2, '2024-11-03 22:55:41.615089', '2', 'Adidas Ultraboost Light', 1, '[{\"added\": {}}]', 7, 1),
(3, '2024-11-03 22:56:33.376783', '3', 'ASICS Gel-Kayano 30', 1, '[{\"added\": {}}]', 7, 1),
(4, '2024-11-03 22:57:44.246698', '4', 'New Balance Fresh Foam 1080v12', 1, '[{\"added\": {}}]', 7, 1),
(5, '2024-11-03 22:58:42.551700', '5', 'Brooks Ghost 15', 1, '[{\"added\": {}}]', 7, 1),
(6, '2024-11-03 23:00:18.665449', '6', 'Hoka One One Clifton 9', 1, '[{\"added\": {}}]', 7, 1),
(7, '2024-11-03 23:01:10.413535', '7', 'Saucony Endorphin Speed 3', 1, '[{\"added\": {}}]', 7, 1),
(8, '2024-11-03 23:02:26.861645', '8', 'Puma Velocity Nitro 2', 1, '[{\"added\": {}}]', 7, 1),
(9, '2024-11-03 23:03:05.423824', '9', 'Under Armour HOVR Machina 3', 1, '[{\"added\": {}}]', 7, 1),
(10, '2024-11-03 23:03:22.688543', '8', 'Puma Velocity Nitro 2', 2, '[{\"changed\": {\"fields\": [\"Imagen\"]}}]', 7, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(9, 'kmStoreApp', 'carrito'),
(10, 'kmStoreApp', 'carritoitem'),
(8, 'kmStoreApp', 'ordenenvio'),
(7, 'kmStoreApp', 'producto'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-11-03 22:48:53.233865'),
(2, 'auth', '0001_initial', '2024-11-03 22:48:53.628850'),
(3, 'admin', '0001_initial', '2024-11-03 22:48:53.726589'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-11-03 22:48:53.734568'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-11-03 22:48:53.742547'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-11-03 22:48:53.800391'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-11-03 22:48:53.859235'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-11-03 22:48:53.897134'),
(9, 'auth', '0004_alter_user_username_opts', '2024-11-03 22:48:53.907106'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-11-03 22:48:53.945005'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-11-03 22:48:53.947997'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-11-03 22:48:53.954978'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-11-03 22:48:53.979912'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-11-03 22:48:54.003848'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-11-03 22:48:54.027783'),
(16, 'auth', '0011_update_proxy_permissions', '2024-11-03 22:48:54.036759'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-11-03 22:48:54.060695'),
(18, 'kmStoreApp', '0001_initial', '2024-11-03 22:48:54.196255'),
(19, 'kmStoreApp', '0002_remove_carrito_cantidad_and_more', '2024-11-03 22:48:54.792588'),
(20, 'sessions', '0001_initial', '2024-11-03 22:48:54.831501');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `kmstoreapp_carrito`
--

CREATE TABLE `kmstoreapp_carrito` (
  `id` bigint(20) NOT NULL,
  `usuario_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

--
-- Volcado de datos para la tabla `kmstoreapp_carrito`
--

INSERT INTO `kmstoreapp_carrito` (`id`, `usuario_id`) VALUES
(1, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `kmstoreapp_carritoitem`
--

CREATE TABLE `kmstoreapp_carritoitem` (
  `id` bigint(20) NOT NULL,
  `cantidad` int(10) UNSIGNED NOT NULL CHECK (`cantidad` >= 0),
  `carrito_id` bigint(20) NOT NULL,
  `producto_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `kmstoreapp_ordenenvio`
--

CREATE TABLE `kmstoreapp_ordenenvio` (
  `id` bigint(20) NOT NULL,
  `direccion` varchar(200) NOT NULL,
  `ciudad` varchar(100) NOT NULL,
  `region` varchar(100) NOT NULL,
  `codigo_postal` varchar(10) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `email` varchar(254) NOT NULL,
  `fecha_orden` datetime(6) NOT NULL,
  `completado` tinyint(1) NOT NULL,
  `usuario_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `kmstoreapp_producto`
--

CREATE TABLE `kmstoreapp_producto` (
  `id` bigint(20) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `descripcion` longtext NOT NULL,
  `precio` decimal(10,2) NOT NULL,
  `stock` int(10) UNSIGNED NOT NULL,
  `imagen` varchar(100) DEFAULT NULL
) ;

--
-- Volcado de datos para la tabla `kmstoreapp_producto`
--

INSERT INTO `kmstoreapp_producto` (`id`, `nombre`, `descripcion`, `precio`, `stock`, `imagen`) VALUES
(1, 'Nike Air Zoom Pegasus 40', 'Ligera y versátil para entrenamientos diarios.', 130000.00, 10, 'productos/pegasus.png'),
(2, 'Adidas Ultraboost Light', 'Amortiguación de alto retorno de energía para largas distancias.', 190000.00, 5, 'productos/adidas_ultraboost.jpg'),
(3, 'ASICS Gel-Kayano 30', 'Excelente estabilidad y soporte para pronadores.', 160000.00, 8, 'productos/ASICS-GEL-KAYANO-30.jpg'),
(4, 'New Balance Fresh Foam 1080v12', 'Comodidad de alto nivel con amortiguación Fresh Foam.', 160000.00, 15, 'productos/NB_fresh_foam.jpg'),
(5, 'Brooks Ghost 15', 'Suave y adaptable, ideal para todo tipo de corredores.', 140000.00, 10, 'productos/Brooks_Ghost_15.jpg'),
(6, 'Hoka One One Clifton 9', 'Amortiguación máxima con sensación ligera.', 145000.00, 10, 'productos/Hoka_One_One_Clifton_9.png'),
(7, 'Saucony Endorphin Speed 3', 'Zapatilla rápida con placa de nailon para mayor impulso.', 170000.00, 5, 'productos/Saucony_Endorphin_Speed_3.jpg'),
(8, 'Puma Velocity Nitro 2', 'Amortiguación reactiva y gran tracción.', 120000.00, 4, 'productos/PUMA_Velocity_Nitro_2_1.jpg'),
(9, 'Under Armour HOVR Machina 3', 'Amortiguación HOVR y conectividad para seguimiento de carrera.', 150000.00, 10, 'productos/Under_Armour_HOVR_Machina_3.jpeg');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `kmstoreapp_carrito`
--
ALTER TABLE `kmstoreapp_carrito`
  ADD PRIMARY KEY (`id`),
  ADD KEY `kmStoreApp_carrito_usuario_id_3d75b471_fk_auth_user_id` (`usuario_id`);

--
-- Indices de la tabla `kmstoreapp_carritoitem`
--
ALTER TABLE `kmstoreapp_carritoitem`
  ADD PRIMARY KEY (`id`),
  ADD KEY `kmStoreApp_carritoit_carrito_id_bd20c7ad_fk_kmStoreAp` (`carrito_id`),
  ADD KEY `kmStoreApp_carritoit_producto_id_dc61f59f_fk_kmStoreAp` (`producto_id`);

--
-- Indices de la tabla `kmstoreapp_ordenenvio`
--
ALTER TABLE `kmstoreapp_ordenenvio`
  ADD PRIMARY KEY (`id`),
  ADD KEY `kmStoreApp_ordenenvio_usuario_id_a7863fe6_fk_auth_user_id` (`usuario_id`);

--
-- Indices de la tabla `kmstoreapp_producto`
--
ALTER TABLE `kmstoreapp_producto`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT de la tabla `kmstoreapp_carrito`
--
ALTER TABLE `kmstoreapp_carrito`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `kmstoreapp_carritoitem`
--
ALTER TABLE `kmstoreapp_carritoitem`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `kmstoreapp_ordenenvio`
--
ALTER TABLE `kmstoreapp_ordenenvio`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `kmstoreapp_producto`
--
ALTER TABLE `kmstoreapp_producto`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `kmstoreapp_carrito`
--
ALTER TABLE `kmstoreapp_carrito`
  ADD CONSTRAINT `kmStoreApp_carrito_usuario_id_3d75b471_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `kmstoreapp_carritoitem`
--
ALTER TABLE `kmstoreapp_carritoitem`
  ADD CONSTRAINT `kmStoreApp_carritoit_carrito_id_bd20c7ad_fk_kmStoreAp` FOREIGN KEY (`carrito_id`) REFERENCES `kmstoreapp_carrito` (`id`),
  ADD CONSTRAINT `kmStoreApp_carritoit_producto_id_dc61f59f_fk_kmStoreAp` FOREIGN KEY (`producto_id`) REFERENCES `kmstoreapp_producto` (`id`);

--
-- Filtros para la tabla `kmstoreapp_ordenenvio`
--
ALTER TABLE `kmstoreapp_ordenenvio`
  ADD CONSTRAINT `kmStoreApp_ordenenvio_usuario_id_a7863fe6_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
