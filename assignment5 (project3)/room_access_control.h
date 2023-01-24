/*
 *   File: room_access_control.h
 * Author: Hayan Al-Machnouk
 *   Date: 2023/01/24
 *
 * This header file contains the function prototypes for a multithreaded 
 * patient room access control program in a hospital. The program uses 
 * pthreads to control access to the room by doctors and visitors.
 *
 * The program enforces the following rules:
 * 1. Doctors can enter the room one at a time, and can enter only if no visitors are in the room.
 * 2. A visitor can only enter the room if no doctors are in the room and if a maximum of 2 other visitors
 *    are in the room (three in total).
 * 3. When a doctor arrives, he must wait for all the current visitors in the room to leave the room.
 * 4. When a doctor arrives, no more visitors are allowed in, until a waiting doctor enters and leaves the room.
 * 5. When a doctor leaves the room, only one waiting doctor or up to three waiting visitors can enter the room, depending on who comes first.
 */

#ifndef ROOM_ACCESS_CONTROL_H
#define ROOM_ACCESS_CONTROL_H

#include <pthread.h>

/* =============================================================================
 * thread function responsible for controlling doctor access to the room.
 * =============================================================================
 */
void* doctor_thread(void* arg);

/* =============================================================================
 * thread function responsible for controlling visitor access to the room.
 * =============================================================================
 */
void* visitor_thread(void* arg);

/* =============================================================================
 * thread function responsible for printing the current status of the room.
 * =============================================================================
 */
void* display_thread(void* arg);

/* =============================================================================
 * function handles arguments and initializes program and creates the threads. 
 * When finished sends cancellation signals to all threads, and releases all resources.
 * =============================================================================
 */
int main(int argc, char* argv[]);

#endif