import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('http://localhost:5000/');
  await page.getByRole('link', { name: '5', exact: true }).click();
  await expect(page.locator('body')).toContainText('Der Mitarbeiter hat gar nix');
});