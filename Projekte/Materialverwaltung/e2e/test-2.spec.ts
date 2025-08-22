import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://localhost:5000/');
  await page.getByRole('link', { name: 'Materialliste' }).click();
  await expect(page.getByRole('heading')).toHaveText("Material-Liste")
});