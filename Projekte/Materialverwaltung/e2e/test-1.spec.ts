import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
await page.goto('http://localhost:5000/');
await page.getByRole('link', { name: 'Material hinzufügen' }).click();
await page.getByRole('textbox', { name: 'typ' }).click();
await page.getByRole('textbox', { name: 'typ' }).fill('Schlüssel');
await page.getByRole('textbox', { name: 'seriennummer' }).click();
await page.getByRole('textbox', { name: 'seriennummer' }).fill('25003');
await page.getByRole('textbox', { name: 'kaufdatum' }).fill('2025-06-05');
await page.getByRole('button', { name: 'Material anlegen' }).click();
await page.getByRole('link', { name: 'Materialliste' }).click();
await expect(page.getByRole('rowgroup')).toContainText('25003');
  // Recording...
});