-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Player`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Player` (
  `idPlayer` INT NOT NULL AUTO_INCREMENT,
  `PName` VARCHAR(45) NOT NULL,
  `PLastName` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idPlayer`),
  UNIQUE INDEX `idPlayer_UNIQUE` (`idPlayer` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Stadium`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Stadium` (
  `SCode` INT NOT NULL AUTO_INCREMENT,
  `SAddress` VARCHAR(45) NOT NULL,
  `SCapacity` INT NOT NULL,
  `SDateOpening` DATE NOT NULL,
  `SLastRenov` DATE NOT NULL,
  PRIMARY KEY (`SCode`),
  UNIQUE INDEX `SCode_UNIQUE` (`SCode` ASC),
  UNIQUE INDEX `SAddress_UNIQUE` (`SAddress` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Team`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Team` (
  `TName` VARCHAR(45) NOT NULL,
  `YearOfFund` DATE NOT NULL,
  `Stadium_SCode` INT NOT NULL,
  PRIMARY KEY (`TName`, `Stadium_SCode`),
  UNIQUE INDEX `TName_UNIQUE` (`TName` ASC),
  INDEX `fk_Team_Stadium1_idx` (`Stadium_SCode` ASC),
  CONSTRAINT `fk_Team_Stadium1`
    FOREIGN KEY (`Stadium_SCode`)
    REFERENCES `mydb`.`Stadium` (`SCode`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Game`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Game` (
  `GDate` VARCHAR(45) NOT NULL,
  `GType` INT NOT NULL,
  `GScore` INT NOT NULL,
  `GCode` VARCHAR(45) NOT NULL,
  `Team_TName1` VARCHAR(45) NOT NULL,
  `Team_TName2` VARCHAR(45) NOT NULL,
  UNIQUE INDEX `GDate_UNIQUE` (`GDate` ASC),
  PRIMARY KEY (`GCode`, `Team_TName2`, `Team_TName1`),
  UNIQUE INDEX `Gamescol_UNIQUE` (`GCode` ASC),
  INDEX `fk_Game_Team1_idx` (`Team_TName1` ASC),
  INDEX `fk_Game_Team2_idx` (`Team_TName2` ASC),
  CONSTRAINT `fk_Game_Team1`
    FOREIGN KEY (`Team_TName1`)
    REFERENCES `mydb`.`Team` (`TName`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Game_Team2`
    FOREIGN KEY (`Team_TName2`)
    REFERENCES `mydb`.`Team` (`TName`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Player_has_played_Team`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Player_has_played_Team` (
  `Player_idPlayer` INT NOT NULL,
  `Team_TName` VARCHAR(45) NOT NULL,
  `ContractDate` DATE NOT NULL,
  PRIMARY KEY (`Player_idPlayer`, `Team_TName`, `ContractDate`),
  INDEX `fk_Player_has_Team_Team1_idx` (`Team_TName` ASC),
  INDEX `fk_Player_has_Team_Player_idx` (`Player_idPlayer` ASC),
  UNIQUE INDEX `Player_idPlayer_UNIQUE` (`Player_idPlayer` ASC),
  UNIQUE INDEX `Team_TName_UNIQUE` (`Team_TName` ASC),
  CONSTRAINT `fk_Player_has_Team_Player`
    FOREIGN KEY (`Player_idPlayer`)
    REFERENCES `mydb`.`Player` (`idPlayer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Player_has_Team_Team1`
    FOREIGN KEY (`Team_TName`)
    REFERENCES `mydb`.`Team` (`TName`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Player_scored_in_Game`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Player_scored_in_Game` (
  `Player_idPlayer` INT NOT NULL,
  `Game_GCode` VARCHAR(45) NOT NULL,
  `GoalsPos` INT UNSIGNED NULL,
  `GoalsNeg` INT NULL,
  PRIMARY KEY (`Player_idPlayer`, `Game_GCode`),
  INDEX `fk_Player_has_Game_Game1_idx` (`Game_GCode` ASC),
  INDEX `fk_Player_has_Game_Player1_idx` (`Player_idPlayer` ASC),
  CONSTRAINT `fk_Player_has_Game_Player1`
    FOREIGN KEY (`Player_idPlayer`)
    REFERENCES `mydb`.`Player` (`idPlayer`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Player_has_Game_Game1`
    FOREIGN KEY (`Game_GCode`)
    REFERENCES `mydb`.`Game` (`GCode`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
