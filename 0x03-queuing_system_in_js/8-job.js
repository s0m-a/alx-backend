#!/usr/bin/yarn dev
import { Queue, Job } from 'kue';

/**
 * Creates push notification jobs
 * @param {Job[]} jobList - Array of jobs to create.
 * @param {Queue} notificationQueue - The Kue queue instance.
 */
export const createPushNotificationsJobs = (jobList, notificationQueue) => {
  if (!(jobList instanceof Array)) {
    throw new Error('jobList is not an array');
  }
  for (const jobInfo of jobList) {
    const job = notificationQueue.create('push_notification_code_3', jobInfo);

    job
      .on('enqueue', () => {
        console.log('Notification job created:', job.id);
      })
      .on('complete', () => {
        console.log('Notification job', job.id, 'completed');
      })
      .on('failed', (err) => {
        console.log('Notification job', job.id, 'failed:', err.message || err.toString());
      })
      .on('progress', (progress, _data) => {
        console.log('Notification job', job.id, `${progress}% complete`);
      });
    job.save();
  }
};

export default createPushNotificationsJobs;
